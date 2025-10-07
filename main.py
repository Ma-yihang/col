import streamlit as st
import base64
import time
st.title("验证身份")
st.subheader("请输入密码:")
x = st.text_input("")
if x == "@MYH201215#zghtr2025424":
    def main_bg(main_bg):
        main_bg_ext = "png"
        st.markdown(
            f"""
             <style>
             .stApp {{
                 background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
                 background-size: cover
             }}
             </style>
             """,
            unsafe_allow_html=True
        )
     
    #调用
    main_bg('bg3.png')
    
    def sidebar_bg(side_bg):
     
       side_bg_ext = 'png'
     
       st.markdown(
          f'''
          <style>
          [data-testid="stSidebar"] > div:first-child {{
              background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
          }}
          </style>
          ''',
          unsafe_allow_html=True,
          )
     
    #调用
    sidebar_bg('bg5.png')
    
    #roading = st.progress(0, '开始加载')
    #for i in range(1, 101, 1):
    #    time.sleep(0.02)
    #   roading.progress(i, '正在加载'+str(i)+'%')
    #roading.progress(100, '加载完毕！')
    
    page = st.sidebar.radio('运动会纪念站',['首页','100米短跑','实心球','200米短跑','400米中长跑','4×100米接力','尾声'])
    
    if page == "首页":
        st.audio('青春夏日-徐梦圆.mp3', loop=True, autoplay=True)
        st.title("运动会纪念")
        st.write('')
        st.write('')
        st.write('''真正的勇气从不是“轻松做到”，而是“明知
                 不易，仍全力以赴”；真正的集体，也从不
                 是少数人的冲锋，而是每个人都愿意为彼此搭
                 把手、为共同的目标拼一把。今天的雨水会慢
                 慢干透，但你们在雨中并肩的模样、在赛场上
                 坚持的身影，会成为咱们班最珍贵的记忆。老
                 师为你们每一个人骄傲，你们都是初二2班的英雄！''')
        #st.write('')
        st.write('----')
        st.image('DSC_3202_01.jpg')
        st.write('----')
        st.link_button('篮球赛网站', 'https://5sbbbxa6zbqx9fcsjxjbqg.streamlit.app/')
    
    
    if page == "100米短跑":
        st.title('100米短跑')
        st.subheader("男子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3223_01.jpg')
        st.image('DSC_3224_01.jpg')
        st.image('DSC_3225_01.jpg')
        st.image('DSC_3228_01.jpg')
        st.image('DSC_3229_01.jpg')
        st.image('DSC_3230_01.jpg')
        st.image('DSC_3232_01.jpg')
        st.image('DSC_3233_01.jpg')
        st.image('DSC_3239_01.jpg')
        st.image('DSC_3240_01.jpg')
        st.image('DSC_3241_01.jpg')
        st.image('DSC_3242_01.jpg')
        st.image('DSC_3243_01.jpg')
        st.image('DSC_3244_01.jpg')
        st.image('DSC_3245_01.jpg')
        st.image('DSC_3246_01.jpg')
        st.image('DSC_3247_01.jpg')
        st.write('----')
        st.video('DSC_3234.mp4')
        st.video('DSC_3235.mp4')
        st.write('----')
        go = st.selectbox('赛场上的每一个瞬间，都藏着让人心头一热的感动！', ['同学们互帮互助⬇', '王浩然拉伤'])
        if go == '王浩然拉伤':
            st.balloons()
            st.write('''王浩然在100米跑中途突发大腿拉伤，从领先的第一名慢慢落后，可他没停下哪怕一步
                     ，忍着剧痛一蹦一跳地冲过终点，直到越过线才撑不住倒下。''')
            st.write('')
            st.write('')
            st.image('DSC_3269.jpg')
            st.write('')
            st.image('DSC_3568.jpg')
            st.write('----')
            #def show_time(t):
            #    st.markdown(str(t))
    
            #st.title('留言栏')
            #recv = st.chat_input('输入你要的内容', on_submit=show_time, args=(time.time(), ))
            #with open('留言.txt', 'r') as file:
            #    content = file.read()
            #    st.write(content)
            #st.divider()
            #if recv:
            #    st.markdown(recv)
    
            #with open("留言.txt", "a") as file:
            #    reca = str(recv) + '//'
            #    file.write(reca)
        st.write('')
        st.write('')
        st.image('DSC_3255_01.jpg')
        st.image('DSC_3261_01.jpg')
        st.image('DSC_3266.jpg')
        st.write('----')
        st.write('')
        st.subheader("女子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3277.jpg')
        st.image('DSC_3278.jpg')
        st.image('DSC_3280.jpg')
        st.image('DSC_3285.jpg')
        st.image('DSC_3289.jpg')
        st.image('DSC_3290.jpg')
        st.image('DSC_3291.jpg')
        st.image('DSC_3293.jpg')
        st.image('DSC_3299.jpg')
        st.image('DSC_3302.jpg')
        st.image('DSC_3303.jpg')
        st.image('DSC_3304.jpg')
            
    if page == "实心球":
        st.title("实心球")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3317.jpg') #图片需压缩
        st.image('DSC_3320.jpg')
        st.write('----')
        st.video('DSC_3323.mp4')
        st.video('DSC_3325.mp4')
        st.video('DSC_3327.mp4')
    
    if page == '200米短跑':
        st.title("200米短跑")
        st.subheader("男子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3345.jpg')
        st.image('DSC_3349.jpg')
        st.image('DSC_3350.jpg')
        st.image('DSC_3351.jpg')
        st.image('DSC_3358.jpg')
        st.image('DSC_3359.jpg')
        st.image('DSC_3360.jpg')
        st.image('DSC_3361.jpg')
        st.image('DSC_3364.jpg')
        st.image('DSC_3365.jpg')
        st.image('DSC_3372.jpg')
        st.image('DSC_3373.jpg')
        st.image('DSC_3374.jpg')
        st.image('DSC_3375.jpg')
        st.image('DSC_3376.jpg')
        st.image('DSC_3377.jpg')
        st.image('DSC_3378.jpg')
        st.write('')
        st.subheader("女子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3390.jpg')
        st.image('DSC_3391.jpg')
        st.image('DSC_3392.jpg')
        st.image('DSC_3393.jpg')
        st.image('DSC_3397.jpg')
        st.image('DSC_3401.jpg')
        st.image('DSC_3402.jpg')
        st.image('DSC_3403.jpg')
        st.image('DSC_3405.jpg')
        st.image('DSC_3406.jpg')
        st.image('DSC_3407.jpg')
        st.image('DSC_3408.jpg')
        st.image('DSC_3409.jpg')
        st.image('DSC_3410.jpg')
        st.image('DSC_3411.jpg')
        st.image('DSC_3412.jpg')
        st.image('DSC_3413.jpg')
        st.image('DSC_3420.jpg')
        st.image('DSC_3421.jpg')
    
    if page == '400米中长跑':
        st.title("400米中长跑")
        st.subheader("男子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3424.jpg')
        st.image('DSC_3425.jpg')
        st.write('')
        st.subheader("女子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3470.jpg')
        st.image('DSC_3471.jpg')
        st.image('DSC_3472.jpg')
        st.image('DSC_3473.jpg')
        st.image('DSC_3474.jpg')
        st.image('DSC_3490.jpg')
        st.image('DSC_3491.jpg')
        st.image('DSC_3492.jpg')
        st.image('DSC_3494.jpg')
        st.image('DSC_3496.jpg')
        st.image('DSC_3497.jpg')    
        st.image('DSC_3498.jpg')
        st.image('DSC_3499.jpg')
        st.image('DSC_3500.jpg')
        st.image('DSC_3504.jpg')
        st.write('')
        st.write('----')
        ch = st.toggle('运动会已经过半…')
        
        message = ''
        if ch:
            st.subheader('是午休时间！')
            st.write('----')
            st.image('DSC_3438.jpg')
            st.image('DSC_3445.jpg')
            st.image('DSC_3457.jpg')
            st.image('DSC_3458.jpg')
            st.image('DSC_3464.jpg')
    
    if page == '4×100米接力':
        st.title('4×100米接力')
        st.subheader("男子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3515.jpg')
        st.image('DSC_3517.jpg')
        st.image('DSC_3519.jpg')
        st.image('DSC_3521.jpg')
        st.image('DSC_3523.jpg')
        st.image('DSC_3526.jpg')
        st.image('DSC_3527.jpg')
        st.image('DSC_3529.jpg')
        st.image('DSC_3530.jpg')
        st.image('DSC_3531.jpg')
        st.image('DSC_3532.jpg')
        st.image('DSC_3537.jpg')
        st.image('DSC_3538.jpg')
        st.image('DSC_3539.jpg')
        st.image('DSC_3546.jpg')
        st.write('')
        st.subheader("女子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3553.jpg')
        st.image('DSC_3554.jpg')
        st.image('DSC_3555.jpg')
        st.image('DSC_3557.jpg')
        st.image('DSC_3558.jpg')
        st.image('DSC_3559.jpg')
        st.image('DSC_3560.jpg')
        st.image('DSC_3562.jpg')
        st.image('DSC_3563.jpg')
        st.image('DSC_3564.jpg')
        st.image('DSC_3565.jpg')
    
    if page == '尾声':
        st.title("结语")
        st.write('')
        st.write('')
        st.write('''''')