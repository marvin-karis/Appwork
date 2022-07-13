console.log('Hello world')
async function start(){
    const response = await fetch("https://api-mobilespecs.azharimm.site/v2/brands/")
    const data = await response.json()
    createBrandList(data.message)
}

start()

function createBrandList(brandList){
    document.getElementById("brands").innerHTML = `
    <select>
          <option>Choose Brand</option>  
          ${Object.keys(brandList).map(function(brand){
              return `<option>${brand}</option>`
          }).join('')}
        </select>
    `
}