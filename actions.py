import argparse
import os
import glob
import sys
import shutil
from typing import Any, NoReturn

# This is to make sure it can still finds its references.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class MaintenanceActions:
    def __init__(self):
        pass

    def remove_logs(self, **kwargs: Any) -> None:
        """Remove all .log files from specified directories."""
        directories = ["logs/debug", "logs/engine", "logs/gameplay", "logs/graphics", "logs/misc", "logs/ursina"]

        for directory in directories:
            log_files = glob.glob(os.path.join(directory, "*.log"))
            for log_file in log_files:
                try:
                    os.remove(log_file)
                    print(f"Removed {log_file}")  # noqa
                except Exception as e:
                    print(f"Failed to remove {log_file}: {e}")  # noqa

    def remove_pycache(self, **kwargs) -> NoReturn:
        """
        Recursively remove all __pycache__ directories from the given base directory.

        :param base_dir: The base directory to start the search.
        """
        counter: int = 0
        for root, dirs, files in os.walk(os.getcwd()):
            for dir_name in dirs:
                if dir_name == "__pycache__":
                    counter += 1
                    dir_path = os.path.join(root, dir_name)
                    shutil.rmtree(dir_path)
        print(f"Removed {counter} __pycache__ directories.")  # noqa

    def generate_classes(self, **kwargs) -> NoReturn:
        import os

        # List of all civics with their names
        civics = [
            "IndividualRights",
            "FreeMarket",
            "RepresentativeDemocracy",
            "SocialWelfare",
            "CivilLiberties",
            "GlobalCooperation",
            "PatrioticEducation",
            "CulturalPreservation",
            "EconomicNationalism",
            "MilitaryStrength",
            "NationalSovereignty",
            "NationalUnity",
            "CollectiveOwnership",
            "WorkersRights",
            "UniversalHealthcare",
            "FreeEducation",
            "SocialEquality",
            "StatePlanning",
            "TotalitarianControl",
            "StatePropaganda",
            "Militarization",
            "CorporateState",
            "NationalPurity",
            "LeaderWorship",
            "ClassAbolition",
            "CommunalLiving",
            "CentralizedEconomy",
            "ProletarianDictatorship",
            "CollectivizedAgriculture",
            "InternationalSolidarity",
            "PrivateProperty",
            "Entrepreneurship",
            "FreeTrade",
            "MinimalRegulation",
            "CapitalAccumulation",
            "MarketCompetition",
            "ElectoralProcess",
            "RuleOfLaw",
            "SeparationOfPowers",
            "HumanRights",
            "ParticipatoryGovernance",
            "TransparentGovernment",
            "HereditaryRule",
            "DivineRight",
            "NobilitySystem",
            "FeudalObligations",
            "CentralizedAuthority",
            "RoyalPatronage",
            "ReligiousLaw",
            "ClericalRule",
            "MoralPolicing",
            "FaithBasedEducation",
            "DivineGovernance",
            "ReligiousUnity",
            "AutocraticRule",
            "StateSurveillance",
            "Censorship",
            "Repression",
            "Propaganda",
            "CentralizedPower",
            "EliteRule",
            "EconomicControl",
            "LimitedParticipation",
            "WealthAccumulation",
            "ExclusiveNetworks",
            "PoliticalManipulation",
            "SelfGovernance",
            "MutualAid",
            "DirectAction",
            "Decentralization",
            "VoluntaryAssociations",
            "Autonomy",
            "CorporateInfluence",
            "LobbyingPower",
            "BusinessPrivileges",
            "EconomicFocus",
            "RegulatoryCapture",
            "CorporateGovernance",
            "ForcedLabor",
            "OwnershipRights",
            "LaborExploitation",
            "SocialHierarchy",
            "Oppression",
            "EconomicDependence",
            "ReligiousDiscipline",
            "MoralPurity",
            "CommunitySurveillance",
            "SimplifiedLiving",
            "ReligiousGovernance",
            "MoralLegislation",
            "ExpertGovernance",
            "ScientificManagement",
            "InnovationFocus",
            "DataDrivenPolicy",
            "EfficientAdministration",
            "Meritocracy",
            "ReasonAndLogic",
            "ScientificInquiry",
            "SecularGovernance",
            "EducationReform",
            "EvidenceBasedPolicy",
            "PhilosophicalDiscourse",
            "CooperativeGovernance",
            "SharedSovereignty",
            "EconomicIntegration",
            "CulturalExchange",
            "CollectiveSecurity",
            "UnifiedPolicy",
        ]

        # Function to convert camel case to snake case
        def camel_to_snake(name):
            return "".join(["_" + i.lower() if i.isupper() else i for i in name]).lstrip("_")

        # Directory to create files in
        directory = "openciv/gameplay/cultures/core"

        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Template for the civic class
        template = """from openciv.gameplay.culture import Civic
        from openciv.engine.managers.i18n import _t


        class {civic}(Civic):
            def __init__(self, *args, **kwargs):
                super().__init__(
                    key="core.culture.civics.{civic_key}",
                    name=_t("content.culture.civics.core.{civic_key}.name"),
                    description=_t("content.culture.civics.core.{civic_key}.description"),
                    *args,
                    **kwargs,
                )
        """

        # Create an empty Python file for each civic using the template
        for civic in civics:
            civic_snake_case = camel_to_snake(civic)
            filename = f"{directory}/{civic_snake_case}.py"
            with open(filename, "w") as file:
                file.write(template.format(civic=civic, civic_key=civic_snake_case))

        print("Civic files have been created with the template.")  # noqa


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Maintenance actions script")
    parser.add_argument("function_name", type=str, help="The name of the function to call")
    known_args, unknown_args = parser.parse_known_args()

    kwargs = {}
    for arg in unknown_args:
        if arg.startswith("--"):
            key, value = arg.split("=")
            key = key.lstrip("--")
            kwargs[key] = value

    return known_args, kwargs


def main() -> None:
    known_args, kwargs = parse_args()
    action_name = known_args.function_name

    actions = MaintenanceActions()
    if hasattr(actions, action_name):
        method = getattr(actions, action_name)
        method(**kwargs)
    else:
        print(f"Function {action_name} not found.")  # noqa


if __name__ == "__main__":
    main()
