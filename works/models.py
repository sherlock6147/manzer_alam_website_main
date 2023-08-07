from django.db import models


# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    isPublished = models.BooleanField(default=False)
    isCaseStudy = models.BooleanField(default=False)
    isFavouraite = models.BooleanField(default=False)
    publishedDate = models.DateTimeField(null=True, blank=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    modifiedOn = models.DateTimeField(auto_now=True)
    importanceScore = models.IntegerField(default=1)
    views = models.IntegerField(blank=True, null=True, default=0)
    heroImage = models.ImageField("Hero Image", upload_to="heroImages/", blank=True, null=True)

    def __str__(self) -> str:
        p_status = "NOT PUBLISHED"
        if self.isPublished:
            p_status = "PUBLISHED"
        return p_status + " " + self.title
