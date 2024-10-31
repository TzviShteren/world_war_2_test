from flask import Flask
from app.gql.query import Query
from app.gql.mutation import Mutation
from graphene import Schema
from flask_graphql import GraphQLView

schema = Schema(query=Query, mutation=Mutation)

app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
    )
)


if __name__ == '__main__':
    app.run()
