org_chart_large = {
    "name": "CEO",
    "subordinates": [
        {
            "name": "CTO",
            "subordinates": [
                {
                    "name": "Development",
                    "subordinates": [
                        {"name": "Engineering Manager"},
                        {
                            "name": "Software Engineers",
                            "subordinates": [
                                {"name": "Senior Developer"},
                                {"name": "Developer"},
                                {"name": "Junior Developer"}
                            ]
                        }
                    ]
                },
                {
                    "name": "QA",
                    "subordinates": [
                        {"name": "QA Manager"},
                        {"name": "QA Engineers"}
                    ]
                }
            ]
        },
        {
            "name": "CFO",
            "subordinates": [
                {"name": "Finance Manager"},
                {
                    "name": "Accounting",
                    "subordinates": [
                        {"name": "Senior Accountant"},
                        {"name": "Junior Accountant"}
                    ]
                }
            ]
        },
        {
            "name": "COO",
            "subordinates": [
                {
                    "name": "Operations",
                    "subordinates": [
                        {"name": "Operations Manager"},
                        {"name": "Logistics Team"}
                    ]
                },
                {
                    "name": "HR",
                    "subordinates": [
                        {"name": "HR Manager"},
                        {"name": "Recruitment Team"}
                    ]
                }
            ]
        }
    ]
}

tech_company_org_chart_2 = {
    "name": "CEO",
    "subordinates": [
        {
            "name": "CTO",
            "subordinates": [
                {
                    "name": "Engineering",
                    "subordinates": [
                        {"name": "Engineering Manager"},
                        {"name": "Development Team"}
                    ]
                },
                {
                    "name": "Product",
                    "subordinates": [
                        {"name": "Product Manager"},
                        {"name": "UX/UI Design Team"}
                    ]
                }
            ]
        },
        {
            "name": "CFO",
            "subordinates": [
                {"name": "Finance Manager"},
                {"name": "Accounting Team"}
            ]
        },
        {
            "name": "COO",
            "subordinates": [
                {
                    "name": "Operations",
                    "subordinates": [
                        {"name": "Operations Manager"},
                        {"name": "Logistics Team"}
                    ]
                },
                {
                    "name": "HR",
                    "subordinates": [
                        {"name": "HR Manager"},
                        {"name": "Recruitment Team"}
                    ]
                }
            ]
        }
    ]
}

tech_company_org_chart_3 = {
    "name": "CEO",
    "subordinates": [
        {
            "name": "CTO",
            "subordinates": [
                {
                    "name": "Software Development",
                    "subordinates": [
                        {"name": "Development Manager"},
                        {
                            "name": "Software Engineers",
                            "subordinates": [
                                {"name": "Frontend Developer"},
                                {"name": "Backend Developer"},
                                {"name": "DevOps Engineer"}
                            ]
                        }
                    ]
                },
                {
                    "name": "Data Science",
                    "subordinates": [
                        {"name": "Data Science Manager"},
                        {"name": "Data Scientists"}
                    ]
                }
            ]
        },
        {
            "name": "CFO",
            "subordinates": [
                {"name": "Finance Manager"},
                {"name": "Financial Analysts"}
            ]
        },
        {
            "name": "COO",
            "subordinates": [
                {
                    "name": "Operations",
                    "subordinates": [
                        {"name": "Operations Manager"},
                        {"name": "Quality Assurance Team"}
                    ]
                },
                {
                    "name": "HR",
                    "subordinates": [
                        {"name": "HR Manager"},
                        {"name": "Employee Relations Team"}
                    ]
                }
            ]
        }
    ]
}
def count_workers(comp_json):
    counter = 1 
    for subordinate in comp_json.get("subordinates",[]):
        counter += count_workers(subordinate)
    return counter

def count_under_cto(comp_json):
    counter = 0
    for subordinate in comp_json.get("subordinates",[]):
        if subordinate["name"] == "CTO":
            counter += count_workers(subordinate)
    return counter

def count_developers(comp_json):
    counter = 0
    for subordinate in comp_json.get("subordinates", []):
        if "Development" in subordinate["name"] :
            print(counter)
            print("00000000000000000000000000000000000")
            counter += count_workers(subordinate)
    return counter



def count_departments(comp_json):
    counter = []
    for subordinate in comp_json.get("subordinates", []):
        if subordinate["name"] not in counter:
            counter.append(subordinate["name"])
    return len(counter)

print(count_workers(org_chart_large))  # Output: 23
print(count_under_cto(org_chart_large))  # Output: 8
print(count_developers(org_chart_large))  # Output: 6
print(count_departments(org_chart_large))  # Output: 9
print(count_workers(tech_company_org_chart_2))  # Output: 16
print(count_under_cto(tech_company_org_chart_2))  # Output: 6
print(count_developers(tech_company_org_chart_2))  # Output: 2
print(count_departments(tech_company_org_chart_2))  # Output: 7
print(count_workers(tech_company_org_chart_3))  # Output: 20
print(count_under_cto(tech_company_org_chart_3))  # Output: 8
print(count_developers(tech_company_org_chart_3))  # Output: 3
print(count_departments(tech_company_org_chart_3))

