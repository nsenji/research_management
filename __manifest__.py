{
    "name": "Research Management",
    "version": "1.0",
    "sequence": -110,
    "summary": "A tool to manage research activities",
    "description": """
A tool to manage research activities
    """,
    "category": "research management",
    
    "depends": ["base", "mail"],
    "data": [
      'views/research_management_views.xml',
      'security/ir.model.access.csv',
      'report/research_report_actions.xml',
      'report/research_report_template.xml'
    ], 
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
