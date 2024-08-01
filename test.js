const fruits = [
  { name: 'pineapple', color: 'yellow' },
  { name: 'apple', color: 'red' },
  { name: 'banana', color: 'yellow' },
  { name: 'strawberry', color: 'red' },
];

const fruitsGroupByColor = Object.groupBy(
  fruits,
  (fruits, index) => fruits.color
);

console.log('fruitsGroupByColor:', fruitsGroupByColor);
