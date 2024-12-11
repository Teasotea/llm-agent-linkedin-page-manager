from gpt_researcher import GPTResearcher

def get_report(query: str, report_type: str) -> str:
    """
    Generates a report based on the given query and report type.

    Args:
        query (str): The search query string.
        report_type (str): The type of report to generate. Must be one of
            'research_report', 'resource_report', or 'outline_report'.

    Returns:
        str: The generated report as a string.
    """
    researcher = GPTResearcher(query, report_type)
    research_result = researcher.conduct_research()
    report = researcher.write_report()
    return report