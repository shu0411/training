let hasValue: boolean = true;

let count: number = 10;
let float: number = 3.14;
let negative: number = -0.12;

let single: string = 'hello';
let double: string = "gn";
let back: string = `gm`;

//型推論できないときだけ型注釈をつける
let hello;
let hello2: string;

//オブジェクト
const person:{
    name: string;
    age: number;
} = {
    name: 'Jack',
    age: 21,
}

console.log(person.name + "は" + person.age + "歳です。")

const person2 = {
    name: {
        first: 'Jack',
        last: 'Smith'
    },
    age: 23,
}

console.log(person2.name.first + ' ' + person2.name.last + "は" + person2.age + "歳です。")

//Array型
const fruits: string[] = ['test', 'test2', 'test3'] 
fruits.push('test4');
console.log(fruits);

//Tuple型
const book: [string, number, boolean] = ['test', 21, false] 
console.log(book);