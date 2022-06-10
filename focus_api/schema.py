import graphene
import graphql_jwt
from tasks.schema import schema as tasks


class Query(tasks.Query, graphene.ObjectType):
    pass

# Mutation:
# - token_auth - for Login
# - refresh_token - for Token refresh
# + schema from api.schema.Mutation


class Mutation(tasks.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass


# Create schema
schema = graphene.Schema(query=Query, mutation=Mutation)
