###

-> encode password using passlib


#### adding JWT
in resources using 

```from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt) ```

so return jwt access_token and refresh_token

if you want to protected page, using `@jwt_required`

So, first of all, this resource has jwt_refresh_token_required decorator, which means that you can access this path only using refresh token. By the way, you cannot access jwt_required endpoints using refresh token, 
and you cannot access jwt_refresh_token_required endpoints using access token. 
This adds an additional layer of security. To identify user we use helper function get_jwt_identity() which extract identity from refresh token. Then we use this identity to generate a new access token and return it to the user.

## Logout and token revoking
Adding logout functionality will require a bit more coding. In contrast to session authorization, 
we cannot just delete tokens on the client side 
because these tokens still will be valid (as long as they don’t expire). 
Thus in case of user logout, we need to add these tokens to the blacklist.
 Then you need to check all incoming tokens against the blacklist and if there is a match — disallow access.
Here is the simplest implementation of logout functionality. 
In models.py add revoked token model:

```
class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)
```

It is a simple model which stores a primary key id and jti — unique identifier of the token. It has also add() method which adds token to the database and is_jti_blacklisted() method which do a check if the token is revoked.