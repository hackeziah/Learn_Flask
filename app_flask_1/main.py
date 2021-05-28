from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'Video(name = {name}, views={views}, likes={likes}'




# db.create_all() to Create DB 


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of Video is Required", required=True)  #help use for error request 
video_put_args.add_argument("views", type=str, help="Views of Video", required=True)#help use for error request 
video_put_args.add_argument("likes", type=str, help="Likes of Video", required=True)#help use for error request 

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of Video is Required", required=True)  #help use for error request 
video_update_args.add_argument("views", type=str, help="Views of Video", required=True)#help use for error request 
video_update_args.add_argument("likes", type=str, help="Likes of Video", required=True)#help use for error request 

resourse_fields = {
    'id' : fields.Integer,
    'name': fields.String,
    'views' : fields.Integer,
    'likes' : fields.Integer,
} #serializers setup

class Video(Resource):
    @marshal_with(resourse_fields) #serializers
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find that ID in Database")
        return result #Objects
    
    @marshal_with(resourse_fields) #serializers
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id already Taken")
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit() #permanent commiting insert
        return video, 201

    @marshal_with(resourse_fields) #serializers
    def patch(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(409, message="Does not exist Cannot be Update")
        
        if 'name' in args:
            result.name =  args['name']
        if 'views' in args:
            result.views =  args['views']
        if 'likes' in args:
            result.likes =  args['likes']

        db.session.add(result)
        db.session.commit() #permanent commiting insert
        return result
        

    def delete(self, video_id):
        abort_if_video_doesnt_exist(video_id)
        del videos[videos]
        return '', 204
    def post(self):
        return {"data": "Posted"}

api.add_resource(Video, "/video/<int:video_id>") #http://127.0.0.1:5000/video/1?name=Comedy&views=3&likes=22


if __name__=="__main__":
    app.run(debug=True)

# def abort_if_video_doesnt_exist(video_id):
#     if video_id not in videos:
#         abort(404, massage= "Video Does Not Exists...")

# def abort_if_video_already_exists(video_id):
#     if video_id in videos:
#         abort(409, massage= "Video Already Exists the ID...")

# class Video(Resource):
#     def get(self, video_id):
#         abort_if_video_doesnt_exist(video_id)
#         return videos[video_id]
    
#     def put(self, video_id):
#         abort_if_video_already_exists(video_id)
#         args =  video_put_args.parse_args()
#         videos[video_id] = args
#         return videos[video_id], 201
    
#     def delete(self, video_id):
#         abort_if_video_doesnt_exist(video_id)
#         del videos[videos]
#         return '', 204


# def abort_if_video_doesnt_exist(video_id):
#     if video_id not in videos:
#         abort(404, massage= "Video Does Not Exists...")

# def abort_if_video_already_exists(video_id):
#     if video_id in videos:
#         abort(409, massage= "Video Already Exists the ID...")





# @app.route("/")
# def welcome():
#     return "Welcome to Atmos  Yeh"