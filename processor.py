# custom_parser.py
import re
from typing import Union
from git.objects.commit import Commit
from semantic_release import CommitParser, ParseResultType, ParsedCommit, ParseError, LevelBump, ParserOptions


class OpencivParsedCommit(ParsedCommit):
    pass


class OpencivParseError(ParseError):
    pass


OpencivParseResult = ParseResultType[OpencivParsedCommit, OpencivParseError]


class OpencivParserOptions(ParserOptions):
    def __init__(self, message_prefix: str = "") -> None:
        self.prefix = message_prefix


class OpencivCommitParser(CommitParser[OpencivParseResult, OpencivParserOptions]):
    parser_options = OpencivParserOptions

    def __init__(self, options: OpencivParserOptions) -> None:
        self.options = options

    def parse(self, commit: Commit) -> OpencivParseResult:
        message = commit.message.decode("utf-8") if isinstance(commit.message, bytes) else commit.message
        header = message.split("\n")[0]

        emoji_dict = {
            "art": "🎨",
            "zap": "⚡️",
            "fire": "🔥",
            "bug": "🐛",
            "ambulance": "🚑️",
            "sparkles": "✨",
            "memo": "📝",
            "rocket": "🚀",
            "lipstick": "💄",
            "tada": "🎉",
            "white_check_mark": "✅",
            "lock": "🔒️",
            "closed_lock_with_key": "🔐",
            "bookmark": "🔖",
            "rotating_light": "🚨",
            "construction": "🚧",
            "green_heart": "💚",
            "arrow_down": "⬇️",
            "arrow_up": "⬆️",
            "pushpin": "📌",
            "construction_worker": "👷",
            "chart_with_upwards_trend": "📈",
            "recycle": "♻️",
            "heavy_plus_sign": "➕",
            "heavy_minus_sign": "➖",
            "wrench": "🔧",
            "hammer": "🔨",
            "globe_with_meridians": "🌐",
            "pencil2": "✏️",
            "poop": "💩",
            "rewind": "⏪️",
            "twisted_rightwards_arrows": "🔀",
            "package": "📦️",
            "alien": "👽️",
            "truck": "🚚",
            "page_facing_up": "📄",
            "boom": "💥",
            "bento": "🍱",
            "wheelchair": "♿️",
            "bulb": "💡",
            "beers": "🍻",
            "speech_balloon": "💬",
            "card_file_box": "🗃️",
            "loud_sound": "🔊",
            "mute": "🔇",
            "busts_in_silhouette": "👥",
            "children_crossing": "🚸",
            "building_construction": "🏗️",
            "iphone": "📱",
            "clown_face": "🤡",
            "egg": "🥚",
            "see_no_evil": "🙈",
            "camera_flash": "📸",
            "alembic": "⚗️",
            "mag": "🔍️",
            "label": "🏷️",
            "seedling": "🌱",
            "triangular_flag_on_post": "🚩",
            "goal_net": "🥅",
            "dizzy": "💫",
            "wastebasket": "🗑️",
            "passport_control": "🛂",
            "adhesive_bandage": "🩹",
            "monocle_face": "🧐",
            "coffin": "⚰️",
            "test_tube": "🧪",
            "necktie": "👔",
            "stethoscope": "🩺",
            "bricks": "🧱",
            "technologist": "🧑‍💻",
            "money_with_wings": "💸",
            "thread": "🧵",
            "safety_vest": "🦺",
        }

        commit_type_dict = {
            "feat": "Features",
            "fix": "Bug Fixes",
            "docs": "Documentation",
            "style": "Styling",
            "refactor": "Refactoring",
            "perf": "Performance Improvements",
            "test": "Testing",
            "build": "Build System",
            "ci": "Continuous Integration",
            "chore": "Chores",
            "revert": "Reverts",
        }

        # Skip merge commits
        if re.search(r"^Merge branch", message):
            return OpencivParseError(commit=commit, error="Merge commit")

        split_message = message.split("\n")
        processed_lines = []
        for line in split_message:
            # Convert :emoji: syntax to actual emojis
            line = re.sub(
                r":([a-zA-Z0-9_]+):",
                lambda match: emoji_dict.get(match.group(1), match.group(0)),
                line,
            )
            processed_lines.append(line)
        commit["message"] = "\n".join(processed_lines)

        # Add type category if present in the message
        type_match = re.match(r"^(\w+):", split_message[0])
        if type_match:
            commit_type = type_match.group(1)
            commit["type"] = commit_type_dict.get(commit_type, "Other")

        bump = self.determine_bump(commit["type"], message)

        parsed_commit = OpencivParsedCommit(
            bump=bump,
            type=commit.get("type", ""),
            scope="",
            descriptions=commit["message"].split("\n\n"),
            breaking_descriptions=[desc for desc in commit["message"].split("\n\n") if "BREAKING CHANGE" in desc],
            commit=commit,
        )

        return parsed_commit

    def determine_bump(self, commit_type: str, description: str) -> LevelBump:
        """
        Determine the bump level based on commit type and description.
        """
        if "BREAKING CHANGE" in description:
            return LevelBump.MAJOR
        elif commit_type in ("feat", "feature"):
            return LevelBump.MINOR
        elif commit_type in ("fix", "bugfix"):
            return LevelBump.PATCH
        else:
            return LevelBump.NO_RELEASE
