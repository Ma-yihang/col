import streamlit as st
import base64
import time
def main_bg(main_bg):
        main_bg_ext = "png"
        st.markdown(
            f'''
             <style>
             .stApp {{
                 background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
                 background-size: cover
             }}
             </style>
             ''',
            unsafe_allow_html=True
        )

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
    
x = st.text_input("",type ='password')
if x == "yfqh":
    main_bg('bg3-2.png')
    sidebar_bg('bg5-1.png')  
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
        st.image('DSC_3202_01.JPG')
        st.write('----')
        st.link_button('篮球赛网站', 'https://5sbbbxa6zbqx9fcsjxjbqg.streamlit.app/')
    
    
    if page == "100米短跑":
        st.title('100米短跑')
        st.subheader("男子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3223_01.JPG')
        st.image('DSC_3224_01.JPG')
        st.image('DSC_3225_01.JPG')
        st.image('DSC_3228_01.JPG')
        st.image('DSC_3229_01.JPG')
        st.image('DSC_3230_01.JPG')
        st.image('DSC_3232_01.JPG')
        st.image('DSC_3233_01.JPG')
        st.image('DSC_3239_01.JPG')
        st.image('DSC_3240_01.JPG')
        st.image('DSC_3241_01.JPG')
        st.image('DSC_3242_01.JPG')
        st.image('DSC_3243_01.JPG')
        st.image('DSC_3244_01.JPG')
        st.image('DSC_3245_01.JPG')
        st.image('DSC_3246_01.JPG')
        st.image('DSC_3247_01.JPG')
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
            st.image('DSC_3269.JPG')
            st.write('')
            st.image('DSC_3568.JPG')
            st.write('----')
            
        st.write('')
        st.write('')
        st.image('DSC_3255_01.JPG')
        st.image('DSC_3261_01.JPG')
        st.image('DSC_3266.JPG')
        st.write('----')
        st.write('')
        st.subheader("女子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3277.JPG')
        st.image('DSC_3278.JPG')
        st.image('DSC_3280.JPG')
        st.image('DSC_3285.JPG')
        st.image('DSC_3289.JPG')
        st.image('DSC_3290.JPG')
        st.image('DSC_3291.JPG')
        st.image('DSC_3293.JPG')
        st.image('DSC_3299.JPG')
        st.image('DSC_3302.JPG')
        st.image('DSC_3303.JPG')
        st.image('DSC_3304.JPG')
            
    if page == "实心球":
        st.title("实心球")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3317.JPG') #图片需压缩
        st.image('DSC_3320.JPG')
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
        st.image('DSC_3345.JPG')
        st.image('DSC_3349.JPG')
        st.image('DSC_3350.JPG')
        st.image('DSC_3351.JPG')
        st.image('DSC_3358.JPG')
        st.image('DSC_3359.JPG')
        st.image('DSC_3360.JPG')
        st.image('DSC_3361.JPG')
        st.image('DSC_3364.JPG')
        st.image('DSC_3365.JPG')
        st.image('DSC_3372.JPG')
        st.image('DSC_3373.JPG')
        st.image('DSC_3374.JPG')
        st.image('DSC_3375.JPG')
        st.image('DSC_3376.JPG')
        st.image('DSC_3377.JPG')
        st.image('DSC_3378.JPG')
        st.write('')
        st.subheader("女子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3390.JPG')
        st.image('DSC_3391.JPG')
        st.image('DSC_3392.JPG')
        st.image('DSC_3393.JPG')
        st.image('DSC_3397.JPG')
        st.image('DSC_3401.JPG')
        st.image('DSC_3402.JPG')
        st.image('DSC_3403.JPG')
        st.image('DSC_3405.JPG')
        st.image('DSC_3406.JPG')
        st.image('DSC_3407.JPG')
        st.image('DSC_3408.JPG')
        st.image('DSC_3409.JPG')
        st.image('DSC_3410.JPG')
        st.image('DSC_3411.JPG')
        st.image('DSC_3412.JPG')
        st.image('DSC_3413.JPG')
        st.image('DSC_3420.JPG')
        st.image('DSC_3421.JPG')
    
    if page == '400米中长跑':
        st.title("400米中长跑")
        st.subheader("男子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3424.JPG')
        st.image('DSC_3425.JPG')
        st.write('')
        st.subheader("女子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3470.JPG')
        st.image('DSC_3471.JPG')
        st.image('DSC_3472.JPG')
        st.image('DSC_3473.JPG')
        st.image('DSC_3474.JPG')
        st.image('DSC_3490.JPG')
        st.image('DSC_3491.JPG')
        st.image('DSC_3492.JPG')
        st.image('DSC_3494.JPG')
        st.image('DSC_3496.JPG')
        st.image('DSC_3497.JPG')    
        st.image('DSC_3498.JPG')
        st.image('DSC_3499.JPG')
        st.image('DSC_3500.JPG')
        st.image('DSC_3504.JPG')
        st.write('')
        st.write('----')
        ch = st.toggle('运动会已经过半…')
        
        message = ''
        if ch:
            st.subheader('是午休时间！')
            st.write('----')
            st.image('DSC_3438.JPG')
            st.image('DSC_3445.JPG')
            st.image('DSC_3457.JPG')
            st.image('DSC_3458.JPG')
            st.image('DSC_3464.JPG')
    
    if page == '4×100米接力':
        st.title('4×100米接力')
        st.subheader("男子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3515.JPG')
        st.image('DSC_3517.JPG')
        st.image('DSC_3519.JPG')
        st.image('DSC_3521.JPG')
        st.image('DSC_3523.JPG')
        st.image('DSC_3526.JPG')
        st.image('DSC_3527.JPG')
        st.image('DSC_3529.JPG')
        st.image('DSC_3530.JPG')
        st.image('DSC_3531.JPG')
        st.image('DSC_3532.JPG')
        st.image('DSC_3537.JPG')
        st.image('DSC_3538.JPG')
        st.image('DSC_3539.JPG')
        st.image('DSC_3546.JPG')
        st.write('')
        st.subheader("女子")
        st.write('----')
        st.write('')
        st.write('')
        st.image('DSC_3553.JPG')
        st.image('DSC_3554.JPG')
        st.image('DSC_3555.JPG')
        st.image('DSC_3557.JPG')
        st.image('DSC_3558.JPG')
        st.image('DSC_3559.JPG')
        st.image('DSC_3560.JPG')
        st.image('DSC_3562.JPG')
        st.image('DSC_3563.JPG')
        st.image('DSC_3564.JPG')
        st.image('DSC_3565.JPG')
    
    if page == '尾声':
        st.title("结语")
        st.write('')
        st.write('')
        st.write('''''')
