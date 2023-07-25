import firebase_admin
from firebase_admin import credentials, db
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from django.conf import settings

# Initialize Firebase SDK (make sure to place your Firebase Admin SDK service account JSON file in the project folder)
cred = credentials.Certificate("treasurehunt-fc698-firebase-adminsdk-wwc8b-e4126ec118.json")
firebase_admin.initialize_app(cred, {'databaseURL': settings.FIREBASE_CONFIG['databaseURL']})

@receiver(post_save, sender=Post)
def sync_post_to_firebase(sender, instance, **kwargs):
    ref = db.reference('/posts')
    post_data = {
        'title': instance.title,
        'content': instance.content,
        'created_at': instance.created_at.isoformat(),
    }
    ref.child(str(instance.id)).set(post_data)
