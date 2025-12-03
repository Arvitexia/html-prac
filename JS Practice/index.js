// let interestRate= 0.3; //variable
// interestRate = 1;
// const increaseRate=2; //constant

// let name='Arvit'; //string
// let age=30; // number
// let isApproved=false; //boolaen
// let firstName; //undefined
// let selectedColor=null; //null value like None in python
    

// let person = {
//     name: 'Arvit',
//     age: 30
// };
// console.log(person);

// //dot notation
// person.name = 'Rezwan';
// console.log(person.name);



//bracket notation;
//ideal to use when user selects the property. here property like 'name'  may be selected by the user which is not [pre defined].
//person[Selection]='Shagoto';
//console.log(person.name);
//arrays
let selectedColors = ['red', 'blue'];
selectedColors[2] = 1
console.log(selectedColors);
console.log(selectedColors[0]);
console.log(selectedColors.length);



//performing functions
function greet(name,lastName) {
    console.log('Hello '+ name+ ' '+ lastName);
}
greet('Arvit', 'Rezwan');
greet('Rezwan')



//calculating functions;
function square(number){
    return number*number
}
console.log(square(2));