from typing import List, Dict

def match_score(resume_keywords: List[str], jd_keywords: List[str]) -> Dict:
    """
    Compute match percentage and missing keywords.
    """
    if not jd_keywords:
        return {"score": 0, "missing": []}

    matched = set(resume_keywords) & set(jd_keywords)
    missing = set(jd_keywords) - set(resume_keywords)

    score = int(len(matched) / len(jd_keywords) * 100)

    return {
        "score": score,
        "missing": list(missing)
    }
