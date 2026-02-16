# PLANNING ---

**Phase 1**
- Define a simple problem statement
- Docstring, type hinting, etc
---
**Phase 2**
- Integrate argparser
---
**Phase 3**
- dummy-plan

---
---

## Phase 1

### Objective
- Implement `docstring` as function description
- Implement type-hinting or type-annotation to the function signature

### Problem Statement 1
**Scenario:** Building an ML pipeline and need to validate incoming data before training. This is a real-world utility that every ML engineer needs for data validation stages in production pipelines. Create a **Data Quality Profiler** that:
- Reads a CSV file
- Calculates basic statistics (missing values, data types, unique counts)
- Detects potential data quality issues (high missing rate, low cardinality)
- Generates a summary report
- Optionally saves the report to a JSON file

### Phase 1 Accomplishments
- Wrote a python script named `data_quality_profiler.py`
- 