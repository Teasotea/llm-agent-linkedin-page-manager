from gpt_researcher import GPTResearcher

def get_report(query: str, report_type: str) -> str:
    """
    :param query: search query
    :param report_type: research_report, resource_report, or outline_report

    :return: research report
    """
    researcher = GPTResearcher(query, report_type)
    research_result = researcher.conduct_research()
    report = researcher.write_report()
    return report

# get_report("what team may win the NBA finals?", "research_report")