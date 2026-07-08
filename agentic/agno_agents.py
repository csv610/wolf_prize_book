
m agno.agent import Agent
from agno.models.litellm import LiteLLM

MODEL = LiteLLM(model="ollama/gemma3")


# ==========================================================
# Discovery Agent
# ==========================================================
discovery_agent = Agent(
    name="Wolf Prize Discovery Agent",
    model=MODEL,
    role="Research Wolf Prize award information.",
    instructions=[
        "Identify the Wolf Prize category.",
        "Identify award year.",
        "Identify laureate(s).",
        "Identify official citation.",
        "Identify the reason for the award.",
    ],
)

# ==========================================================
# Biography Agent
# ==========================================================
biography_agent = Agent(
    name="Biography Agent",
    model=MODEL,
    role="Research laureate biography.",
    instructions=[
        "Education.",
        "Career timeline.",
        "Academic positions.",
        "Research interests.",
        "Major achievements.",
    ],
)

# ==========================================================
# Historical Context Agent
# ==========================================================
history_agent = Agent(
    name="Historical Context Agent",
    model=MODEL,
    role="Explain the historical background.",
    instructions=[
        "Describe the state of the field before the discovery.",
        "Historical developments.",
        "Previous breakthroughs.",
    ],
)

# ==========================================================
# Scientific Background Agent
# ==========================================================
background_agent = Agent(
    name="Scientific Background Agent",
    model=MODEL,
    role="Explain prerequisite knowledge.",
    instructions=[
        "Explain required scientific concepts.",
        "Describe previous theories.",
        "Identify open challenges.",
    ],
)

# ==========================================================
# Contribution Agent
# ==========================================================
contribution_agent = Agent(
    name="Contribution Agent",
    model=MODEL,
    role="Describe prize-winning contributions.",
    instructions=[
        "Summarize discoveries.",
        "Identify key breakthroughs.",
        "Explain significance.",
    ],
)

# ==========================================================
# Innovation Agent
# ==========================================================
innovation_agent = Agent(
    name="Innovation Agent",
    model=MODEL,
    role="Identify innovations.",
    instructions=[
        "New theories.",
        "New algorithms.",
        "New methodologies.",
        "New technologies.",
    ],
)

# ==========================================================
# Publications Agent
# ==========================================================
publication_agent = Agent(
    name="Publication Agent",
    model=MODEL,
    role="Collect landmark publications.",
    instructions=[
        "Most influential papers.",
        "Books.",
        "Patents.",
        "Seminal publications.",
    ],
)

# ==========================================================
# Methodology Agent
# ==========================================================
methodology_agent = Agent(
    name="Methodology Agent",
    model=MODEL,
    role="Explain research methodology.",
    instructions=[
        "Experimental methods.",
        "Computational methods.",
        "Mathematical methods.",
        "Laboratory techniques.",
    ],
)

# ==========================================================
# Applications Agent
# ==========================================================
applications_agent = Agent(
    name="Applications Agent",
    model=MODEL,
    role="Research applications.",
    instructions=[
        "Scientific applications.",
        "Industrial applications.",
        "Medical applications.",
        "Engineering applications.",
    ],
)

# ==========================================================
# Impact Agent
# ==========================================================
impact_agent = Agent(
    name="Impact Agent",
    model=MODEL,
    role="Research impact.",
    instructions=[
        "Scientific impact.",
        "Technological impact.",
        "Economic impact.",
        "Societal impact.",
    ],
)

# ==========================================================
# Collaboration Agent
# ==========================================================
collaboration_agent = Agent(
    name="Collaboration Agent",
    model=MODEL,
    role="Research collaborations.",
    instructions=[
        "Major collaborators.",
        "Research groups.",
        "Institutions.",
    ],
)

# ==========================================================
# Awards Agent
# ==========================================================
awards_agent = Agent(
    name="Awards Agent",
    model=MODEL,
    role="Research other awards.",
    instructions=[
        "Nobel Prize.",
        "Fields Medal.",
        "Abel Prize.",
        "Turing Award.",
        "National Academies.",
    ],
)

# ==========================================================
# Nobel Connection Agent
# ==========================================================
nobel_agent = Agent(
    name="Nobel Connection Agent",
    model=MODEL,
    role="Analyze relationship with Nobel Prize.",
    instructions=[
        "Determine whether the laureate later received a Nobel Prize.",
        "Explain similarities between Wolf Prize and Nobel Prize recognition.",
        "Identify overlapping discoveries.",
    ],
)

# ==========================================================
# Legacy Agent
# ==========================================================
legacy_agent = Agent(
    name="Legacy Agent",
    model=MODEL,
    role="Research long-term legacy.",
    instructions=[
        "Influence on future research.",
        "Major follow-up discoveries.",
        "Current research directions.",
    ],
)

# ==========================================================
# Timeline Agent
# ==========================================================
timeline_agent = Agent(
    name="Timeline Agent",
    model=MODEL,
    role="Generate timeline.",
    instructions=[
        "Career timeline.",
        "Research milestones.",
        "Award timeline.",
    ],
)

# ==========================================================
# Educational Agent
# ==========================================================
education_agent = Agent(
    name="Educational Agent",
    model=MODEL,
    role="Generate educational explanations.",
    instructions=[
        "Explain for beginners.",
        "Explain for undergraduate students.",
        "Explain for graduate students.",
        "Explain for researchers.",
    ],
)

# ==========================================================
# References Agent
# ==========================================================
references_agent = Agent(
    name="References Agent",
    model=MODEL,
    role="Collect references.",
    instructions=[
        "Official Wolf Foundation pages.",
        "Research papers.",
        "Books.",
        "Interviews.",
        "Lecture videos.",
    ],
)

# ==========================================================
# Report Agent
# ==========================================================
report_agent = Agent(
    name="Report Agent",
    model=MODEL,
    role="Generate final report.",
    instructions=[
        "Merge all agent outputs.",
        "Create executive summary.",
        "Generate bibliography.",
        "Produce markdown report.",
    ],
)

# ==========================================================
# Wolf Prize Research Team
# ==========================================================
WOLF_PRIZE_TEAM = [
    discovery_agent,
    biography_agent,
    history_agent,
    background_agent,
    contribution_agent,
    innovation_agent,
    publication_agent,
    methodology_agent,
    applications_agent,
    impact_agent,
    collaboration_agent,
    awards_agent,
    nobel_agent,
    legacy_agent,
    timeline_agent,
    education_agent,
    references_agent,
    report_agent,
]

# ==========================================================
# Run Wolf Prize Research
# ==========================================================
def run_wolf_prize_research(topic: str):

    print("=" * 80)
    print("Wolf Prize Research Pipeline")
    print("=" * 80)

    results = {}

    # Run all agents except Report Agent
    for agent in WOLF_PRIZE_TEAM[:-1]:

        print(f"\nRunning {agent.name}...")

        try:
            response = agent.run(topic)

            if hasattr(response, "content"):
                results[agent.name] = response.content
            else:
                results[agent.name] = str(response)

        except Exception as ex:
            results[agent.name] = f"ERROR: {ex}"

    # -------------------------------------------------------
    # Prepare Report Prompt
    # -------------------------------------------------------

    report_prompt = f"""
Generate a comprehensive Wolf Prize research report.

Research Topic:
{topic}

The following information was collected by specialist agents.

"""

    for name, output in results.items():

        report_prompt += f"""

==================================================
{name}
==================================================

{output}

"""

    print("\nGenerating Final Report...\n")

    report = report_agent.run(report_prompt)

    if hasattr(report, "content"):
        return report.content

    return str(report)


# ==========================================================
# Save Report
# ==========================================================
def save_report(report: str, filename: str):

    with open(filename, "w", encoding="utf-8") as fp:
        fp.write(report)

    print(f"\nReport saved to {filename}")

import argparse


def get_parser():

    parser = argparse.ArgumentParser(
        prog="wolf_prize.py",
        formatter_class=argparse.RawTextHelpFormatter,
        description="""
Wolf Prize Research System

The Wolf Prize is one of the world's most prestigious international awards
recognizing outstanding achievements in science and the arts.

History
-------
• Established by the Wolf Foundation in Israel.
• The Foundation was created in 1975 by Ricardo Wolf.
• The first Wolf Prizes were awarded in 1978.

Scientific Categories
---------------------
• Agriculture
• Chemistry
• Mathematics
• Medicine
• Physics

Arts Categories (Rotating)
--------------------------
• Architecture
• Music
• Painting
• Sculpture

Purpose
-------
To recognize individuals whose achievements contribute to:
• the advancement of science and the arts,
• the benefit of humanity,
• and friendly relations among peoples.

Prize
-----
Each Wolf Prize includes:
• A diploma
• A monetary award (currently US$100,000)

Eligibility
-----------
• Awarded only to individuals (not institutions).
• Open to candidates of any nationality.
• No discrimination based on race, religion, gender, or political views.
• Self-nominations are not accepted.
• Candidates must be nominated by qualified nominators.
• Selection is made by international expert committees appointed by the
  Wolf Foundation.
• The award recognizes outstanding scientific or artistic achievements,
  often representing a lifetime of influential work.

Examples
--------
python wolf_prize.py "Andrew Wiles"

python wolf_prize.py "2025 Wolf Prize in Physics"

python wolf_prize.py "Ada Yonath"

python wolf_prize.py "Graph Theory"

Official Website
----------------
https://wolffund.org.il
"""
    )

    parser.add_argument(
        "topic",
        nargs="?",
        help="Wolf Prize winner, year, category, or research topic"
    )

    return parser


def main():

    parser = get_parser()
    args = parser.parse_args()

    if args.topic is None:
        parser.print_help()
        return

    report = run_wolf_prize_research(args.topic)

    print(report)


if __name__ == "__main__":
    main()


# ==========================================================
# Main
# ==========================================================
def main():

    print("=" * 80)
    print("Wolf Prize Research System")
    print("=" * 80)

    topic = input(
        "\nEnter Wolf Prize winner or topic: "
    ).strip()

    if not topic:
        print("No topic entered.")
        return

    report = run_wolf_prize_research(topic)

    print("\n")
    print("=" * 100)
    print("FINAL REPORT")
    print("=" * 100)
    print(report)

    filename = (
        topic.replace(" ", "_")
             .replace("/", "_")
             .replace("\\", "_")
        + "_WolfPrize.md"
    )

    save_report(report, filename)


# ==========================================================
# Entry Point
# ==========================================================
if __name__ == "__main__":
    main()



