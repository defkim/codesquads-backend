from django.db import models

class Project(models.Model):
	DAYS, MONTHES = range(2)
	DURATION_UNIT = (
		(DAYS, 'Days'),
		(MONTHES, 'Monthes')
	)

	LOWER, MODERATE, HIGH = range(3)
	RANK = (
		(LOWER, 'Lower risk portfolios'),
		(MODERATE, 'Moderate risk portfolios'),
		(HIGH, 'High risk portfolio')
	)

	RECRUITING, PROCESSING, CLOSED = range(3)
	STATUS = (
		(RECRUITING, 'Member wanted'),
		(PROCESSING, 'Project is on-going'),
		(CLOSED, 'Project is finished')
	)

	title = models.CharField(
		max_length=256
	)
	summary = models.CharField(
		max_length=1024
	)
	project_doc = models.TextField()
	duration = models.PositiveSmallIntegerField()
	duration_unit = models.PositiveSmallIntegerField(
		choices=DURATION_UNIT,
		default=RECRUITING
	)
	date_published = models.DateTimeField(
		auto_now_add=True
	)
	score = models.PositiveSmallIntegerField()
	rank = models.PositiveSmallIntegerField(
		choices=RANK,
		default=LOWER
	)
	status = models.PositiveSmallIntegerField(
		choices=STATUS,
		default=RECRUITING
	)
	is_free = models.BooleanField()
	date_created = models.DateTimeField(
		auto_now_add=True
	)
	date_updated = models.DateTimeField(
		auto_now=True
	)

class Group(models.Model):
	project = models.ForeignKey(
		'Project',
		on_delete=models.CASCADE,
		related_name="project_group",
	)
	manager = models.ForeignKey(
		'codeauth.User',
		on_delete=models.CASCADE,
		related_name="user_group",
	)
	# showed via percentage
	progress = models.PositiveSmallIntegerField()
	demo = models.CharField(
		max_length=256
	)
	github_link = models.CharField(
		max_length=256
	)
	date_created = models.DateTimeField(
		auto_now_add=True
	)
	date_updated = models.DateTimeField(
		auto_now=True
	)

class UserProject(models.Model):
	LOWER, MODERATE, HIGH = range(3)
	TROPHY = (
		(LOWER, 'Low level'),
		(MODERATE, 'Seems good'),
		(HIGH, 'Really master')
	)

	user = models.ForeignKey(
		'codeauth.User',
		on_delete=models.CASCADE,
		related_name="user_user_project",
	)
	group = models.ForeignKey(
		'Group',
		on_delete=models.CASCADE,
		related_name="group_user_project",
	)
	is_quit = models.BooleanField()
	trophy = models.PositiveSmallIntegerField(
		choices=TROPHY,
		default=LOWER
	)
	date_created = models.DateTimeField(
		auto_now_add=True
	)
	date_updated = models.DateTimeField(
		auto_now=True
	)
	class Meta:
		unique_together = ("user", "group")

class Order(models.Model):
	SUBMITTED, PASS, FAIL = range(3)
	STATUS = (
		(SUBMITTED, 'Wait for auditing'),
		(PASS, 'Participation allowed'),
		(FAIL, 'Participation forbidden')
	)
	user = models.ForeignKey(
		'codeauth.User',
		on_delete=models.CASCADE,
		related_name="user_order",
	)
	group = models.ForeignKey(
		'Group',
		on_delete=models.CASCADE,
		related_name="group_order",
	)
	status = models.PositiveSmallIntegerField(
		choices=STATUS,
		default=SUBMITTED
	)
	date_created = models.DateTimeField(
		auto_now_add=True
	)
	date_updated = models.DateTimeField(
		auto_now=True
	)
	class Meta:
		unique_together = ("user", "group")
