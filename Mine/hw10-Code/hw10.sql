.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes WHERE min < height AND height <= max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child AS name FROM parents, dogs WHERE parent = name ORDER BY height DESC;


-- Sentences about siblings that are the same size

CREATE TABLE siblings AS
  SELECT a.child AS a, b.child AS b FROM parents AS a, parents AS b WHERE a.parent = b.parent AND a.child < b.child;

CREATE TABLE sentences AS
  SELECT "The two siblings, " || a || " plus " || b || " have the same size: "|| x.size FROM siblings, size_of_dogs AS x, size_of_dogs AS y
  WHERE a = x.name AND b = y.name AND x.size = y.size;
