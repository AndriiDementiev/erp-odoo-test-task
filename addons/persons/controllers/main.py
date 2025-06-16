from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError


class PersonsController(http.Controller):

    @http.route("/persons", type="http", auth="public", website=True)
    def list_persons(self, **kw):
        persons = request.env["persons.person"].sudo().search([], order="id desc", limit=5)
        return request.render("persons.persons_website_template", {"persons": persons})

    @http.route("/persons/new", type="http", auth="public", website=True)
    def persons_form(self, **kw):
        return request.render("persons.person_form_template")

    @http.route("/persons/create", type="http", auth="public", methods=["POST"], website=True)
    def create_person(self, **kw):
        vals = {
            "first_name": kw.get("first_name"),
            "last_name": kw.get("last_name"),
            "birthday": kw.get("birthday"),
            "sex": kw.get("sex"),
            "company_id": request.env.company.id,
        }
        try:
            request.env["persons.person"].sudo().create(vals)
        except AccessError:
            return request.redirect("/persons?error=access")
        return request.redirect("/persons?success=1")
