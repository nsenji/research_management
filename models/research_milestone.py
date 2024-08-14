from odoo import models, fields, api

class ResearchMilestone(models.Model):
    _name = 'research.milestone'
    _description = 'Research Milestone'

    name = fields.Char(string='Milestone Name', required=True)
    description = fields.Text(string='Description')
    due_date = fields.Date(string='Due Date')
    completion_date = fields.Date(string='Completion Date')
    status = fields.Selection([
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('delayed', 'Delayed')
    ], string='Status', default='planned')
    project_id = fields.Many2one('research.management', string='Research Project', required=True, ondelete='cascade')