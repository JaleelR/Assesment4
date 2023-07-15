"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy


# DO NOT MODIFY THIS FUNCTION
db = SQLAlchemy()




def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)




class Playlist(db.Model):
    """Playlist."""
    __tablename__ = "playlists"
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name  = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=True)
   
    # ADD THE NECESSARY CODE HERE
    

class Song(db.Model):
    """Song."""
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    artist = db.Column(db.String(20), nullable=False)
    # ADD THE NECESSARY CODE HERE
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=True)
    playlist = db.relationship("Playlist", backref="songs")




class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
 # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlistsongs"
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable = False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable = False)





