test = {
  'name': 'Question 3: In and Out',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = 3
          >>> def out(g, m):
          ...    x = 5 * m
          ...    def inner():
          ...        return x
          ...    if m == 0:
          ...        return g
          ...    else:
          ...        return out(inner, m-1)
          >>> v = out(out, 1)()
          >>> v
          7f26a14774d51f0b58e7b44a760bd7c0
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
