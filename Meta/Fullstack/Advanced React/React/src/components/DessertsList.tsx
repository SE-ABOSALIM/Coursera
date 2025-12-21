/* React "Keys" for list elements */
type Dessert = {
  id: number;
  name: string;
  calories: number;
  createdAt: string;
};

type Data = {
  data: Dessert[];
};

function DessertsList(props: Data) {
  const { data } = props;
  const itemsList = data
    .filter((dessert) => {
      return dessert.calories < 500;
    })
    .sort((a, b) => {
      return a.calories - b.calories;
    })
    .map((dessert) => {
      return (
        <li key={dessert.id}>
          {dessert.name} - {dessert.calories}
        </li>
      );
    });
  return (
    <div>
      <ul>{itemsList}</ul>
    </div>
  );
}

export default DessertsList;
