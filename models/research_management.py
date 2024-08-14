from odoo import models, fields, api

class ResearchManagement(models.Model):
    _name = 'research.management'
    _description = 'Research Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Research Title', required=True)
    lead_researcher_id = fields.Many2one('res.partner', string='Lead Researcher')
    research_team_ids = fields.Many2many('res.partner', string='Research Team')
    abstract = fields.Html(string='Research Abstract')
    funding_secured = fields.Boolean(string='Funding Secured')
    active = fields.Boolean(string='Active Research', default=True, tracking = True)
    stage = fields.Selection([
        ('proposal', 'Proposal'),
        ('literature_review', 'Literature Review'),
        ('data_collection', 'Data Collection'),
        ('data_analysis', 'Data Analysis'),
        ('writing', 'Writing'),
        ('peer_review', 'Peer Review'),
        ('published', 'Published')
    ], string='Research Stage', default='proposal', tracking=True)
    document_ids = fields.Many2many('ir.attachment', string='Research Documents')
    milestone_ids = fields.One2many('research.milestone', 'project_id', string='Research Milestones')


    