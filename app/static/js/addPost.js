const form = document.querySelector('form')
const newParagraph = document.querySelector('#new-p-btn')
const submitBtn = form.querySelector('button')
form.addEventListener('submit',(e)=>{
    e.preventDefault()

    let data = new FormData(form)
    let text = []
    let params = new URLSearchParams(window.location.search)
    let token = document.querySelector('user-btn') ? document.querySelector('user-btn').getAttribute('data-t') ? document.querySelector('user-btn').getAttribute('data-t') : null : null
    console.log(params.get('token'),token)
    form.querySelectorAll('textarea').forEach(ele=>{
        text.push(ele.value)
    })
    data.set('text',JSON.stringify(text))
    if(params.get('token') != null){
        data.append('token',params.get('token'))
        fetch(`/api/add-post/`,{method:'POST',body:data}).then((res)=>res.json()).then((jres)=>{
            if(jres.success){
                console.log(data)
                alert("Post Added")
                form.querySelectorAll('input').forEach(ele=>{
                    ele.value = ''
                })
                form.querySelector('textarea').value = ''
            }else{
                alert(JSOn.stringify(jres))
            }
        }).catch((e)=>{alert(JSON.stringify(e))})
    }else{
        alert("You need to Log in")
    }
})

newParagraph.addEventListener('click',()=>{
    let textarea = document.createElement('textarea')
    textarea.setAttribute('class','w-full border-2 border-gray-400 focus:outline-none p')
    textarea.setAttribute('placeholder','New Paragraph')
    textarea.setAttribute('rows',1)
    textarea.setAttribute('cols','30')
    textarea.setAttribute('required',true)
    form.insertBefore(textarea,submitBtn)
})