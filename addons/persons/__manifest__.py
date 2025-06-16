{
    "name": "Persons",
    "version": "16.0.1.0.0",
    "summary": "Manage persons via backend and website",
    "description": "Advanced Persons module with webhook-ready controllers, "
                   "frontend form, access controls, and documentation in README.",
    "category": "Website",
    "author": "Andrii Dementiev",
    "license": "LGPL-3",
    "depends": ["base", "website"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/person_views.xml",
        "views/website_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "persons/static/css/persons.css",
            "persons/static/js/persons.js",
        ],
    },
    "application": False,
    "installable": True,
}
