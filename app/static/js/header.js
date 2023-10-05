resEle = document.querySelector('#res')
Bar = document.querySelector('#search')

handleScreenSChange = ()=>{
    const viewportWidth = window.innerWidth
    console.log("Changed")
    if(Bar.classList.contains('hidden') || viewportWidth < 760){
        Bar = document.querySelector('#search-sm')
        resEle = document.querySelector('#res-sm')
    }
    else{
        Bar = document.querySelector('#search')
        resEle = document.querySelector('#res')
    }
}

handleScreenSChange()
window.addEventListener('resize',handleScreenSChange)


Bar.addEventListener('focus',(e)=>{
})

Bar.addEventListener('keyup',()=>{
    let container = resEle
    container.innerHTML = ''

    fetch('/api/posts/search',{headers:{"Content-Type":"application/json"},method:'POST',body:JSON.stringify({"term":Bar.value})}).then((res)=>res.json()).then((jres)=>{

        if(jres.length > 0){
            resEle.classList.remove('hidden')
            Array.from(jres).forEach(post => {
                container.innerHTML = 
                `
                <a href="/api/post/get/?post_id=${post.id}">
                    <div class="post bg-Whitish px-1 py-2 w-full cursor-pointer hover:bg-gray-300">
                        <div class="flex w-full space-x-3">
                            <img src="/api${post.image}" class="w-[6rem] h-[5rem]" alt="">
                            <div class="flex flex-col">
                                <h1 class="text-gray-500 font-bold">${post.title}</h1>
                                <p>${post.content}</p>
                            </div>
                        </div>
                    </div>
                </a>
                `
            })}else{
                resEle.classList.add('hidden')
            }

    }).catch((e)=>{
        console.log(e)
    })
})

console.log(Bar)