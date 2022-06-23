let val = prompt("what would you like to do?");
const todos = ["Collect Eggs", "Clean Litter"];
while(val !== "quit") {
    if (val === "list"){
        console.log("***************")
        for(let i = 0; i< todos.length; i++) {
            console.log(`${i}: ${todos[i]}`);
        }
        console.log("***************")
    }
    else if (val === 'new') {
        const newTodo = prompt("what is new todo?");
        todos.push(newTodo);
        console.log(`${newTodo} added to the list`);
    }
    else if (val === 'delete') {
        // could check invalid index
        const index  = prompt("enter an index:");
        const deleted = todos.splice(index,1);
        console.log(`Ok deleted ${deleted[0]}`)
    }
    
    val = prompt("what would you like to do?");
    
}
console.log("You quitter!")