
let userToken = document.querySelector('#user-btn') ? document.querySelector('#user-btn').getAttribute('data-t') : null

let commentForm = document.querySelector('#commentForm')
let message = commentForm.querySelector('input')
commentForm.addEventListener('submit',(e)=>{
    e.preventDefault()
    let params = new URLSearchParams(window.location.search)
    if(params.get('token') == '' || params.get('token') == null){
        alert("You need to log in")
    }
    else{
        if(userToken != null){
            if(message.value != null || message.value != ''){
                fetch("/api/comment/",{method:'POST',headers:{"Content-type":"application/json"},body:JSON.stringify({"token":params.get('token'),"text":message.value,"post_id":commentForm.getAttribute('data-d')})}).then((res)=>res.json()).then((jres)=>{
                    if(jres.success){
                        fetch("/api/refresh-comments/",{method:'POST',headers:{"Content-type":"application/json"},body:JSON.stringify(jres)}).then((re)=>re.json()).then((commentJres)=>{
                            let commentsWrapper  = document.querySelector('#comments')
                            let div = document.createElement('div')
                            div.setAttribute('class','comment')

                            let username = document.createElement('p')
                            username.setAttribute('class','text-gray-400')
                            username.textContent = commentJres.username

                            let comment = document.createElement('p')
                            comment.textContent = commentJres.comment

                            div.appendChild(username)
                            div.append(comment)
                            commentsWrapper.appendChild(div)
                        }).catch((er)=>alert(er))
                    }
                }).catch((e)=>alert(e))
            }
        }
    }
})



{/* <div class="comment">
<p class="text-gray-400">Chris240</p>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis, adipisci laborum libero tenetur earum provident!</p>
</div> */}