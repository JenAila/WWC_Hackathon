from django.db import models

class KojojoItems(models.Model):
    unique_id   = models.CharField(max_length=255, primary_key=True)
    title_name = models.CharField(max_length=200)
    title_url = models.CharField(max_length=200)
    title_price = models.CharField(max_length=200)
    title_title = models.CharField(max_length=200)
    title_location = models.CharField(max_length=200)
    title_message = models.CharField(max_length=200)
    title_pic = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    Load_Date = models.DateTimeField('date published')

    class Meta:
        managed = False
        db_table='kojojo_items'
    # def __str__(self):
    #     return self.title_name

# class Board(models.Model):
#     name = models.CharField(max_length=30, unique=True)
#     description = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name


# class Topic(models.Model):
#     subject = models.CharField(max_length=255)
#     last_updated = models.DateTimeField(auto_now_add=True)
#     board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
#     starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)


# class Post(models.Model):
#     message = models.TextField(max_length=4000)
#     topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(null=True)
#     created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
#     updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
