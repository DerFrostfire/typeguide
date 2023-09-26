
// Type with literals
let favoriteColor = 'red';

//Generics
// < T > is used for example but we can use < X > or < A > etc.
const addId = < T >(obj:T) => {
	let id = Math.floor(Math.random() * 1000);
  
    return { ...obj, id };
};
 