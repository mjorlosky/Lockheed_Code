console.log("Before");
let random = Math.random();
if (random < 0.5) {
    console.log("Rand");
}
console.log("After");
const day = 2;
switch (day) {
    case 1:
        console.log("monday")
        break;
    case 2:
        console.log("tuesday")
        break;
}
let days = ["monday","tuesday","wednesday"]
console.log(days[0]+days.length)
days.push("thursday")
console.log(days[3]+days.length)
console.log(days.slice(1))
// splice (index, remove num, item to add)
days.splice(0,0,"sunday")
console.log(days)
//.sort()
const nums = [1,2,3]
nums[0] = 3
console.log(nums)
// nums = [] error
const person = {firstname: "mike", lastname: "orlosky"}
console.log(person)
const subreddits = ['cringe','books','chickens']
for (let sub of subreddits) { // use in instead of of for objects keys
    console.log(`Visit reddit.com/r/${sub}`)
}