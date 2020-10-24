function findShort(s)
{
  
  return Math.min(...s.split(' ').map(({ length }) => length));
  
}
