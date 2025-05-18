from django.contrib.auth.models import User
from django.test import TestCase
from ..serializers import UserSerializers


class UserSerializersTestCase(TestCase):
    
    def setUp(self):
        self.user1 = User.objects.create(username = 'Diro',
                                         first_name = 'Adnrue', 
                                         last_name = 'Cherlov', 
                                         email = 'famas.god1231@gmail.com', 
                                         )
        
        
        self.user1.set_password('20031983aA')
        self.user1.save()
    
    def test_ok(self):
        serializers1 = UserSerializers(self.user1).data
        
        serializers2 = {
            'username' : 'Diro',
            'first_name' : 'Adnrue',
            'last_name' : 'Cherlov',
            'email' : 'famas.god1231@gmail.com',
        }
        
        self.assertEqual(serializers1, serializers2)