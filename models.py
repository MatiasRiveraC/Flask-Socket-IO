# coding: utf-8
from setup import db


t_activity = db.Table(
    'activity',
    db.Column('id', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('design', db.ForeignKey('public.designs.id')),
    db.Column('session', db.ForeignKey('public.sessions.id')),
    schema='public'
)



class ActorSelection(db.Model):
    __tablename__ = 'actor_selection'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    description = db.Column(db.Text, nullable=False)
    orden = db.Column(db.Integer)
    actorid = db.Column(db.ForeignKey('public.actors.id'))
    uid = db.Column(db.ForeignKey('public.users.id'))
    stageid = db.Column(db.ForeignKey('public.stages.id'))
    stime = db.Column(db.DateTime, server_default=db.FetchedValue())

    actor = db.relationship('Actor', primaryjoin='ActorSelection.actorid == Actor.id', backref='actor_selections')
    stage = db.relationship('Stage', primaryjoin='ActorSelection.stageid == Stage.id', backref='actor_selections')
    user = db.relationship('User', primaryjoin='ActorSelection.uid == User.id', backref='actor_selections')



class Actor(db.Model):
    __tablename__ = 'actors'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String, nullable=False)
    jorder = db.Column(db.Boolean, nullable=False)
    stageid = db.Column(db.ForeignKey('public.stages.id'))
    justified = db.Column(db.Boolean, server_default=db.FetchedValue())
    word_count = db.Column(db.Integer, server_default=db.FetchedValue())

    stage = db.relationship('Stage', primaryjoin='Actor.stageid == Stage.id', backref='actors')



class Chat(db.Model):
    __tablename__ = 'chat'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    sesid = db.Column(db.ForeignKey('public.sessions.id'))
    stageid = db.Column(db.ForeignKey('public.stages.id'))
    uid = db.Column(db.ForeignKey('public.users.id'))
    content = db.Column(db.Text)
    stime = db.Column(db.DateTime, server_default=db.FetchedValue())
    parent_id = db.Column(db.ForeignKey('public.chat.id'))

    parent = db.relationship('Chat', remote_side=[id], primaryjoin='Chat.parent_id == Chat.id', backref='chats')
    session = db.relationship('Session', primaryjoin='Chat.sesid == Session.id', backref='chats')
    stage = db.relationship('Stage', primaryjoin='Chat.stageid == Stage.id', backref='chats')
    user = db.relationship('User', primaryjoin='Chat.uid == User.id', backref='chats')



class Criterion(db.Model):
    __tablename__ = 'criteria'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.Text, nullable=False)
    pond = db.Column(db.Integer, nullable=False)
    inicio = db.Column(db.Text)
    proceso = db.Column(db.Text)
    competente = db.Column(db.Text)
    avanzado = db.Column(db.Text)
    rid = db.Column(db.ForeignKey('public.rubricas.id'))

    rubrica = db.relationship('Rubrica', primaryjoin='Criterion.rid == Rubrica.id', backref='criteria')



class CriteriaSelection(db.Model):
    __tablename__ = 'criteria_selection'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    selection = db.Column(db.Integer)
    cid = db.Column(db.ForeignKey('public.criteria.id'))
    uid = db.Column(db.ForeignKey('public.users.id'))
    repid = db.Column(db.ForeignKey('public.reports.id'))

    criterion = db.relationship('Criterion', primaryjoin='CriteriaSelection.cid == Criterion.id', backref='criteria_selections')
    report = db.relationship('Report', primaryjoin='CriteriaSelection.repid == Report.id', backref='criteria_selections')
    user = db.relationship('User', primaryjoin='CriteriaSelection.uid == User.id', backref='criteria_selections')



class Design(db.Model):
    __tablename__ = 'designs'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    creator = db.Column(db.ForeignKey('public.users.id'))
    design = db.Column(db.JSON)
    public = db.Column(db.Boolean, server_default=db.FetchedValue())
    locked = db.Column(db.Boolean, server_default=db.FetchedValue())

    user = db.relationship('User', primaryjoin='Design.creator == User.id', backref='designs')



class DesignsDocument(db.Model):
    __tablename__ = 'designs_documents'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    path = db.Column(db.Text, nullable=False)
    dsgnid = db.Column(db.ForeignKey('public.designs.id', ondelete='CASCADE'))
    uploader = db.Column(db.ForeignKey('public.users.id'))
    active = db.Column(db.Boolean, server_default=db.FetchedValue())

    design = db.relationship('Design', primaryjoin='DesignsDocument.dsgnid == Design.id', backref='designs_documents')
    user = db.relationship('User', primaryjoin='DesignsDocument.uploader == User.id', backref='designs_documents')



class Differential(db.Model):
    __tablename__ = 'differential'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    title = db.Column(db.Text, server_default=db.FetchedValue())
    tleft = db.Column(db.Text, nullable=False)
    tright = db.Column(db.Text, nullable=False)
    orden = db.Column(db.Integer, nullable=False)
    creator = db.Column(db.ForeignKey('public.users.id'))
    sesid = db.Column(db.ForeignKey('public.sessions.id'))
    stageid = db.Column(db.ForeignKey('public.stages.id'))
    justify = db.Column(db.Boolean, server_default=db.FetchedValue())
    num = db.Column(db.Integer, server_default=db.FetchedValue())
    word_count = db.Column(db.Integer, server_default=db.FetchedValue())

    user = db.relationship('User', primaryjoin='Differential.creator == User.id', backref='differentials')
    session = db.relationship('Session', primaryjoin='Differential.sesid == Session.id', backref='differentials')
    stage = db.relationship('Stage', primaryjoin='Differential.stageid == Stage.id', backref='differentials')



class DifferentialChat(db.Model):
    __tablename__ = 'differential_chat'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    uid = db.Column(db.ForeignKey('public.users.id'))
    did = db.Column(db.ForeignKey('public.differential.id'))
    content = db.Column(db.Text)
    stime = db.Column(db.DateTime, server_default=db.FetchedValue())
    parent_id = db.Column(db.ForeignKey('public.differential_chat.id'))

    differential = db.relationship('Differential', primaryjoin='DifferentialChat.did == Differential.id', backref='differential_chats')
    parent = db.relationship('DifferentialChat', remote_side=[id], primaryjoin='DifferentialChat.parent_id == DifferentialChat.id', backref='differential_chats')
    user = db.relationship('User', primaryjoin='DifferentialChat.uid == User.id', backref='differential_chats')



t_differential_selection = db.Table(
    'differential_selection',
    db.Column('id', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('uid', db.ForeignKey('public.users.id')),
    db.Column('did', db.ForeignKey('public.differential.id')),
    db.Column('sel', db.Integer, nullable=False),
    db.Column('iteration', db.Integer),
    db.Column('comment', db.Text),
    db.Column('stime', db.DateTime, server_default=db.FetchedValue()),
    schema='public'
)



class Document(db.Model):
    __tablename__ = 'documents'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    title = db.Column(db.Text, nullable=False)
    path = db.Column(db.Text, nullable=False)
    sesid = db.Column(db.ForeignKey('public.sessions.id'))
    uploader = db.Column(db.ForeignKey('public.users.id'))
    active = db.Column(db.Boolean, server_default=db.FetchedValue())

    session = db.relationship('Session', primaryjoin='Document.sesid == Session.id', backref='documents')
    user = db.relationship('User', primaryjoin='Document.uploader == User.id', backref='documents')



t_drafts = db.Table(
    'drafts',
    db.Column('id', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('sesid', db.ForeignKey('public.sessions.id')),
    db.Column('data', db.Text),
    schema='public'
)



t_finish_session = db.Table(
    'finish_session',
    db.Column('uid', db.ForeignKey('public.users.id')),
    db.Column('sesid', db.ForeignKey('public.sessions.id')),
    db.Column('status', db.Integer),
    db.Column('stime', db.DateTime),
    schema='public'
)



class Idea(db.Model):
    __tablename__ = 'ideas'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    content = db.Column(db.Text)
    descr = db.Column(db.Text)
    serial = db.Column(db.String)
    uid = db.Column(db.ForeignKey('public.users.id'))
    docid = db.Column(db.ForeignKey('public.documents.id'))
    orden = db.Column(db.Integer, server_default=db.FetchedValue())
    iteration = db.Column(db.Integer, server_default=db.FetchedValue())
    stime = db.Column(db.DateTime)

    document = db.relationship('Document', primaryjoin='Idea.docid == Document.id', backref='ideas')
    user = db.relationship('User', primaryjoin='Idea.uid == User.id', backref='ideas')
    reports = db.relationship('Report', secondary='public.report_ideas', backref='ideas')



class JigsawRole(db.Model):
    __tablename__ = 'jigsaw_role'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    sesid = db.Column(db.ForeignKey('public.sessions.id'))

    session = db.relationship('Session', primaryjoin='JigsawRole.sesid == Session.id', backref='jigsaw_roles')



t_jigsaw_users = db.Table(
    'jigsaw_users',
    db.Column('stageid', db.ForeignKey('public.stages.id')),
    db.Column('userid', db.ForeignKey('public.users.id')),
    db.Column('roleid', db.ForeignKey('public.jigsaw_role.id')),
    schema='public'
)



class Overlay(db.Model):
    __tablename__ = 'overlays'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    uid = db.Column(db.ForeignKey('public.users.id'))
    qid = db.Column(db.ForeignKey('public.questions.id'))
    type = db.Column(db.String, nullable=False)
    iteration = db.Column(db.Integer)
    geom = db.Column(db.Text, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)

    question = db.relationship('Question', primaryjoin='Overlay.qid == Question.id', backref='overlays')
    user = db.relationship('User', primaryjoin='Overlay.uid == User.id', backref='overlays')



class PassReset(db.Model):
    __tablename__ = 'pass_reset'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    mail = db.Column(db.String, nullable=False)
    token = db.Column(db.String, nullable=False)
    ctime = db.Column(db.DateTime)



t_question_text = db.Table(
    'question_text',
    db.Column('id', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('sesid', db.ForeignKey('public.sessions.id')),
    db.Column('title', db.Text),
    db.Column('content', db.Text),
    schema='public'
)



class Question(db.Model):
    __tablename__ = 'questions'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    content = db.Column(db.Text)
    options = db.Column(db.Text)
    answer = db.Column(db.Integer)
    comment = db.Column(db.Text)
    other = db.Column(db.Text)
    sesid = db.Column(db.ForeignKey('public.sessions.id'))
    textid = db.Column(db.Integer)
    plugin_data = db.Column(db.String)
    cpid = db.Column(db.ForeignKey('public.questions.id'))

    parent = db.relationship('Question', remote_side=[id], primaryjoin='Question.cpid == Question.id', backref='questions')
    session = db.relationship('Session', primaryjoin='Question.sesid == Session.id', backref='questions')



t_report_comment = db.Table(
    'report_comment',
    db.Column('uid', db.ForeignKey('public.users.id')),
    db.Column('repid', db.ForeignKey('public.reports.id')),
    db.Column('comment', db.Text),
    schema='public'
)



t_report_ideas = db.Table(
    'report_ideas',
    db.Column('rid', db.ForeignKey('public.reports.id')),
    db.Column('idea_id', db.ForeignKey('public.ideas.id')),
    schema='public'
)



class ReportPair(db.Model):
    __tablename__ = 'report_pair'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    uid = db.Column(db.ForeignKey('public.users.id'))
    sesid = db.Column(db.ForeignKey('public.sessions.id'))
    repid = db.Column(db.ForeignKey('public.reports.id'))

    report = db.relationship('Report', primaryjoin='ReportPair.repid == Report.id', backref='report_pairs')
    session = db.relationship('Session', primaryjoin='ReportPair.sesid == Session.id', backref='report_pairs')
    user = db.relationship('User', primaryjoin='ReportPair.uid == User.id', backref='report_pairs')



class Report(db.Model):
    __tablename__ = 'reports'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    content = db.Column(db.Text)
    example = db.Column(db.Boolean, server_default=db.FetchedValue())
    rid = db.Column(db.ForeignKey('public.rubricas.id'))
    uid = db.Column(db.ForeignKey('public.users.id'))
    title = db.Column(db.Text)

    rubrica = db.relationship('Rubrica', primaryjoin='Report.rid == Rubrica.id', backref='reports')
    user = db.relationship('User', primaryjoin='Report.uid == User.id', backref='reports')



class Rubrica(db.Model):
    __tablename__ = 'rubricas'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    sesid = db.Column(db.ForeignKey('public.sessions.id'))

    session = db.relationship('Session', primaryjoin='Rubrica.sesid == Session.id', backref='rubricas')



t_selection = db.Table(
    'selection',
    db.Column('answer', db.Integer),
    db.Column('uid', db.ForeignKey('public.users.id'), nullable=False),
    db.Column('comment', db.Text),
    db.Column('qid', db.ForeignKey('public.questions.id'), nullable=False),
    db.Column('iteration', db.Integer),
    db.Column('stime', db.DateTime),
    db.Column('confidence', db.Integer),
    db.Index('selection_pkey', 'uid', 'qid', 'iteration'),
    schema='public'
)



class SemanticDocument(db.Model):
    __tablename__ = 'semantic_document'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    sesid = db.Column(db.ForeignKey('public.sessions.id'))
    orden = db.Column(db.Integer)

    session = db.relationship('Session', primaryjoin='SemanticDocument.sesid == Session.id', backref='semantic_documents')



class SemanticUnit(db.Model):
    __tablename__ = 'semantic_unit'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    sentences = db.Column(db.ARRAY(int))
    comment = db.Column(db.Text)
    uid = db.Column(db.ForeignKey('public.users.id'))
    iteration = db.Column(db.Integer)
    docs = db.Column(db.ARRAY(int))
    sesid = db.Column(db.ForeignKey('public.sessions.id'))

    session = db.relationship('Session', primaryjoin='SemanticUnit.sesid == Session.id', backref='semantic_units')
    user = db.relationship('User', primaryjoin='SemanticUnit.uid == User.id', backref='semantic_units')



class Session(db.Model):
    __tablename__ = 'sessions'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.Text, nullable=False)
    descr = db.Column(db.Text)
    time = db.Column(db.DateTime)
    creator = db.Column(db.ForeignKey('public.users.id'))
    code = db.Column(db.String)
    status = db.Column(db.Integer, server_default=db.FetchedValue())
    type = db.Column(db.String)
    options = db.Column(db.String, server_default=db.FetchedValue())
    archived = db.Column(db.Boolean, server_default=db.FetchedValue())
    current_stage = db.Column(db.ForeignKey('public.stages.id'))

    user = db.relationship('User', primaryjoin='Session.creator == User.id', backref='sessions')
    stage = db.relationship('Stage', primaryjoin='Session.current_stage == Stage.id', backref='sessions')



t_sesusers = db.Table(
    'sesusers',
    db.Column('sesid', db.ForeignKey('public.sessions.id')),
    db.Column('uid', db.ForeignKey('public.users.id')),
    db.Column('device', db.String),
    schema='public'
)



class Stage(db.Model):
    __tablename__ = 'stages'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    number = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String, nullable=False)
    anon = db.Column(db.Boolean, server_default=db.FetchedValue())
    chat = db.Column(db.Boolean, server_default=db.FetchedValue())
    prev_ans = db.Column(db.String)
    sesid = db.Column(db.ForeignKey('public.sessions.id'))
    question = db.Column(db.Text)
    grouping = db.Column(db.String)
    options = db.Column(db.Text)

    session = db.relationship('Session', primaryjoin='Stage.sesid == Session.id', backref='stages')



t_status_record = db.Table(
    'status_record',
    db.Column('sesid', db.ForeignKey('public.sessions.id')),
    db.Column('status', db.Integer),
    db.Column('stime', db.DateTime),
    schema='public'
)



class Team(db.Model):
    __tablename__ = 'teams'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    sesid = db.Column(db.ForeignKey('public.sessions.id'))
    leader = db.Column(db.ForeignKey('public.users.id'))
    original_leader = db.Column(db.ForeignKey('public.users.id'))
    progress = db.Column(db.Integer, server_default=db.FetchedValue())
    stageid = db.Column(db.ForeignKey('public.stages.id'))

    user = db.relationship('User', primaryjoin='Team.leader == User.id', backref='user_user_teams')
    user1 = db.relationship('User', primaryjoin='Team.original_leader == User.id', backref='user_user_teams_0')
    session = db.relationship('Session', primaryjoin='Team.sesid == Session.id', backref='teams')
    stage = db.relationship('Stage', primaryjoin='Team.stageid == Stage.id', backref='teams')
    users = db.relationship('User', secondary='public.teamusers', backref='user_user_teams_1')



t_teamusers = db.Table(
    'teamusers',
    db.Column('tmid', db.ForeignKey('public.teams.id')),
    db.Column('uid', db.ForeignKey('public.users.id')),
    schema='public'
)



class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.Text, nullable=False)
    rut = db.Column(db.Text, nullable=False)
    _pass = db.Column('pass', db.Text, nullable=False)
    mail = db.Column(db.Text, nullable=False)
    sex = db.Column(db.String)
    role = db.Column(db.String)
    aprendizaje = db.Column(db.Enum('Reflexivo', 'Activo', 'Teorico', 'Pragmatico', name='tipo_aprendizaje'))
    section = db.Column(db.String)
    lang = db.Column(db.String, server_default=db.FetchedValue())
