from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta


class Person(models.Model):
    _name = "persons.person"
    _description = "Person"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)

    full_name = fields.Char(
        string="Full Name",
        compute="_compute_full_name",
        store=True,
        readonly=True,
    )

    birthday = fields.Date(string="Birthday")

    age = fields.Integer(
        string="Age",
        compute="_compute_age",
        store=True,
        readonly=True,
    )

    sex = fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
            ("non_binary", "Non-binary")
        ],
        string='Sex'
    )

    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        required=True,
        default=lambda self: self.env.company.id
    )

    @api.depends("first_name", "last_name")
    def _compute_full_name(self):
        for rec in self:
            names = filter(None, [rec.first_name, rec.last_name])
            rec.full_name = ' '.join(names)

    @api.depends("birthday")
    def _compute_age(self):
        for rec in self:
            if rec.birthday:
                today = date.today()
                rec.age = relativedelta(today, rec.birthday).years
            else:
                rec.age = 0
