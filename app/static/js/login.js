const loginForm = document.querySelector('#login_form')
const registerForm = document.querySelector('#register_form')


document.querySelectorAll('textarea').forEach(ele=>{
    ele.addEventListener('focus',()=>{
        ele.setAttribute('rows',30)
    })
})

loginForm.querySelector('a').addEventListener('click',(e)=>{
    e.preventDefault()
    loginForm.classList.toggle('hidden')
    registerForm.classList.toggle('hidden')

    if(loginForm.classList.contains('hidden')){
        console.log("Showing..")
        let image = registerForm.querySelector('img')
        let input = registerForm.querySelector('#profile-image')
        input.addEventListener('change',(event)=>{
            const selectedFile = event.target.files[0];
            if (selectedFile) {
                const reader = new FileReader();
                reader.onload = function () {
                    image.src = reader.result;
                };
                reader.readAsDataURL(selectedFile);
        }})
    }


})

registerForm.querySelector('a').addEventListener('click',(e)=>{
    e.preventDefault()
    loginForm.classList.toggle('hidden')
    registerForm.classList.toggle('hidden')

})

loginForm.addEventListener('submit',(e)=>{
    e.preventDefault()
    let params = new URLSearchParams(window.location.search)
    let formData = new FormData(loginForm)
    formData.append('next',params.get('next'))
    let next = params.get('next')

    fetch(`/api/login/user/?next=${params.get('next')}`,{method:'POST',body:formData}).then((res)=>res.json()).then((jres)=>{
        if(jres){
            if(jres.token){
                window.location.href = `${params.get('next') == null ? '/api/home/':next}?token=${jres.token}`
            }else{
                alert(JSON.stringify(jres))
            }
        }
    }).catch((e)=>alert(e))
})

registerForm.addEventListener('submit',(e)=>{
    e.preventDefault()
    let formData = new FormData(registerForm)
    let params = new URLSearchParams(window.location.search)
    formData.append('next',params.get('next'))
    let next = params.get('next')
    fetch(`/api/register/user/?=${params.get('next')}`,{method:'POST',body:formData}).then((res)=>res.json()).then((jres)=>{
        if(jres){
            if(jres.token){
                window.location.href = `${params.get('next') == null ? '/api/home/':next}?token=${jres.token}`
            }else{
                alert(JSON.stringify(jres))
            }
        }
    }).catch((e)=>alert(e))
})