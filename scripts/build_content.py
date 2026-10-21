"""Build the English and Chinese static pages from shared bilingual content.

Run with Python 3 from any directory. No third-party dependencies are required.
"""
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parents[1]
SHARED = (ROOT / 'content/shared.html').read_text(encoding='utf-8')
ICONS = re.search(r'<svg[\s\S]*?</svg>', SHARED).group(0)
BIB = '\n'.join(re.findall(r'<template[\s\S]*?</template>', SHARED))
VERSION = '20261021'

def icon(name):
    return f'<svg class="ic" aria-hidden="true"><use href="#i-{name}"/></svg>'

def external(url, label):
    return f'<a href="{escape(url, quote=True)}" target="_blank" rel="noopener">{label}</a>'

PAPERS = [
    dict(title='Swimming Under Constraints: A Safe Reinforcement Learning Framework for Quadrupedal Bio-Inspired Propulsion',
         authors='Xinyu Cui*, <b>Fei Han</b>*✉, Hang Xu, Yongcheng Zeng, Luoyang Sun, Ruizhi Zhang, Jian Zhao, Haifeng Zhang, Weikun Li, Hao Chen, Jun Wang, Dixia Fan✉',
         venue='ICRA 2026', status='accepted', img='saferl_framework.jpg', bib='bib-saferl',
         summary=('Studies safe reinforcement learning for quadrupedal swimming, combining force constraints, leg-phase coordination and transfer from single-leg policies to whole-body motion.', '研究四足游动的安全强化学习，将受力约束、腿部相位协调与单腿策略向整机运动的迁移结合起来。'),
         links=[('https://arxiv.org/abs/2603.04073','arXiv'),('https://arxiv.org/pdf/2603.04073v1','PDF'),('#video-icra2026','Video')]),
    dict(title='Learn to Swim: Data-Driven LSTM Hydrodynamic Model for Quadruped Robot Gait Optimization',
         authors='<b>Fei Han</b>, Pengming Guo, Hao Chen, Weikun Li, Jingbo Ren, Naijun Liu, Ning Yang, Dixia Fan✉',
         venue='ICRA 2025 · pp. 10261–10267', status='published', img='lts_experiment.jpg', bib='bib-lts',
         summary=('Builds an LSTM hydrodynamic model from experimental force data and uses it for multi-objective swimming-gait optimization and robot validation.', '基于实验受力数据建立 LSTM 水动力模型，用于多目标游动步态优化，并完成机器人实验验证。'),
         links=[('https://doi.org/10.1109/ICRA55743.2025.11128080','DOI'),('https://arxiv.org/abs/2505.03146','arXiv'),('https://github.com/HanFei-hz/Dog_LSTM','Code'),('#video-icra2025','Video')]),
    dict(title='Exploring Storm Petrel Pattering and Sea-Anchoring Using Deep Reinforcement Learning',
         authors='Jiaqi Xue*, <b>Fei Han</b>*, Brett Klaassen van Oorschot, Glenna Clifton, Dixia Fan✉',
         venue='Bioinspiration &amp; Biomimetics · 2023 · 18(6): 066016', status='published', img='petrel_drl.jpg', bib='bib-petrel',
         summary=('Combines a morphological model, air–water forces and deep reinforcement learning to study storm-petrel pattering and sea-anchoring behaviors.', '结合形态模型、空水耦合受力与深度强化学习，研究海燕的踏水及海锚行为。'),
         links=[('https://doi.org/10.1088/1748-3190/ad00a2','DOI')]),
    dict(title='Force Decomposition on Flapping Flexible Plate via Impulse Theory and Dynamic Mode Decomposition',
         authors='Linlin Kang, Shiying Xiong, Buchen Wu, Chao Li, Mingming Ge, Dehan Yuan, <b>Fei Han</b>, Weicheng Cui',
         venue='Physics of Fluids · 2023 · 35(10): 101914', status='published',
         summary=('Uses impulse theory and dynamic mode decomposition to analyze fluid forces on a flapping flexible plate.', '采用冲量理论与动态模态分解，分析柔性拍动板的流体受力。'),
         links=[('https://doi.org/10.1063/5.0169989','DOI')]),
    dict(title='Propulsive Performance and Vortex Dynamics of Jellyfish-like Propulsion with Burst-and-Coast Strategy',
         authors='Linlin Kang, An-Kang Gao, <b>Fei Han</b>, Weicheng Cui, Xi-Yun Lu',
         venue='Physics of Fluids · 2023 · 35(9): 091904', status='published',
         summary=('Examines the propulsion and vortex dynamics of jellyfish-like motion using a burst-and-coast strategy.', '研究水母式间歇推进中的推进表现及涡动力学机制。'),
         links=[('https://doi.org/10.1063/5.0160878','DOI')]),
    dict(title=('Design of a Composite-Cavity Bioinspired Soft Hand for Underwater Grasping', '面向水下抓取作业的复合腔体仿生软体手设计'),
         authors=('<b>Fei Han</b>, Daohui Zhang, Xingang Zhao, et al.', '<b>韩非</b>，张道辉，赵新刚等'),
         venue=('Robot · 2023 · 45(2): 207–217 · In Chinese', '机器人 · 2023 · 45(2): 207–217'), status='published', img='soft-gripper.jpg',
         summary=('Develops a composite-cavity soft gripper for underwater manipulation, covering structural design, fabrication and experimental evaluation.', '面向水下作业开展复合腔体软体手的结构设计、制作与实验研究。'),
         links=[('https://doi.org/10.13973/j.cnki.robot.210473','DOI')]),
    dict(title=('Human-Robot Interaction Control of a Soft Hand Based on a Curvature Prediction Model', '基于弯曲度预测模型的软体手人机交互控制'),
         authors=('<b>Fei Han</b>, Daohui Zhang, Xingang Zhao', '<b>韩非</b>，张道辉，赵新刚'),
         venue=('Automation &amp; Instrumentation · 2022 · 37(7): 43–47 · In Chinese', '自动化与仪表 · 2022 · 37(7): 43–47'), status='published', img='soft-gripper-control.webp',
         summary=('Models soft-finger bending with an LSTM predictor and develops human–robot interaction control with a data glove.', '通过 LSTM 模型预测软体手指弯曲状态，结合数据手套开展人机交互控制。'),
         links=[('https://doi.org/10.19557/j.cnki.1001-9944.2022.07.009','DOI')]),
    dict(title='An Underwater Soft Claw Based on Bionic Principle',
         authors='Yanxu Sun, <b>Fei Han</b>, Daohui Zhang, Xingang Zhao, Dan Ye',
         venue='IEEE ROBIO · 2021', status='published',
         summary=('Investigates the design and operation of a bioinspired soft claw for underwater grasping.', '研究面向水下抓取的仿生软体抓手设计与操作。'), links=[]),
    dict(title='Embracing Flow Unsteadiness: A High-Throughput Learning Platform Enables Vortex-Exploiting Bioinspired Propulsion',
         authors='<b>Fei Han</b>*, Xinyu Cui*, Zhipeng Wang*, Ning Yang, Hang Xu, Haifeng Zhang, Zhongming Hu, Jun Wang, Junfeng Du, Dixia Fan✉',
         venue='Nature Mechanical Engineering', status='review', img='reef_overview.jpg', bib='bib-reef',
         summary=('REEF combines the SHOAL experimental platform with imitation, offline and online learning to study propulsion policies that exploit unsteady fluid interactions.', 'REEF 将 SHOAL 实验平台与模仿学习、离线学习及在线学习结合，研究利用非定常流体相互作用的推进策略。'),
         links=[('https://arxiv.org/abs/2609.14254','arXiv'),('https://arxiv.org/pdf/2609.14254v1','PDF')]),
    dict(title='From Gaits to Routes: Execution-Aware Hybrid Behavior Planning for Quadrupedal Swimming with Experiment-Calibrated Hydrodynamics',
         venue='ICRA 2027', status='review',
         summary=('Studies hybrid behavior planning and skill distillation for quadrupedal swimming in an experiment-calibrated hydrodynamic simulator.', '在实验校准的水动力仿真环境中，研究四足游动的混合行为规划与技能蒸馏。'), links=[]),
    dict(title='HydroWrench: A Dataset and Benchmark for Dynamic Load Reconstruction in Bioinspired Aquatic Mechanisms',
         venue='ICLR 2027', status='review',
         summary=('Builds a dataset and evaluation benchmark for reconstructing dynamic loads from motion commands in bioinspired aquatic mechanisms.', '构建由运动指令重建水下仿生机构动态载荷的数据集与评估基准。'), links=[]),
]

def build(zh=False):
    def t(en, cn): return cn if zh else en
    def local(value): return value[int(zh)] if isinstance(value, tuple) else value
    def heading(en, cn): return f'<h3 class="section-subtitle">{t(en, cn)}</h3>'
    def theme(title, date, body, image, alt, refs='', fit=False):
        return f'''<article class="theme"><figure class="theme-media"><img src="./assets/img/{image}" alt="{escape(alt)}" loading="lazy" class="{'fit' if fit else ''}"></figure><div class="theme-body"><p class="project-date">{date}</p><h3>{title}</h3><p>{body}</p>{f'<p class="theme-refs">{refs}</p>' if refs else ''}</div></article>'''
    def timeline(rows):
        return '<ol class="timeline">'+''.join(f'<li><time>{date}</time><h4>{title}</h4><p>{body}</p></li>' for date,title,body in rows)+'</ol>'
    nav_names=[('about','About','关于我'),('research','Research','研究项目'),('publications','Publications','论文成果'),('videos','Videos','视频'),('experience','Resume','履历与简历'),('life','Community','校园与服务')]
    nav=''.join(f'<a class="tab-link" id="tab-{id}" href="#{id}" aria-controls="{id}">{t(en,cn)}</a>' for id,en,cn in nav_names)
    lang='zh-CN' if zh else 'en'
    page_url='https://hanfei-hz.github.io/'+('zh.html' if zh else '')
    description=t('Fei Han, PhD student at Westlake University. Bioinspired propulsion, robot learning, hydrodynamic modeling and soft robotics. Expected graduation: June 2027.', '韩非，西湖大学博士研究生。研究仿生推进、机器人学习、水动力建模与软体机器人，预计2027年6月毕业。')
    profile=f'''<aside class="profile-card" aria-label="{t('Profile','个人信息')}">
      <nav class="language-switch" aria-label="{t('Language','语言选择')}"><a href="./index.html?lang=en" data-language="en" lang="en" {'aria-current="page"' if not zh else ''}>English</a><a href="./zh.html?lang=zh" data-language="zh" lang="zh-CN" {'aria-current="page"' if zh else ''}>中文</a></nav>
      <div class="profile-top"><img class="portrait" src="./assets/img/portrait-neutral.jpg" alt="{t('Portrait of Fei Han','韩非个人照片')}" width="560" height="558"><div class="profile-identity"><h1>{t('Fei Han <span lang="zh-CN">韩非</span>','韩非 <span lang="en">Fei Han</span>')}</h1><p class="role-label">{t('Ph.D. Student','博士研究生')}</p><p class="profile-affiliation">{t('Westlake University','西湖大学')}</p></div></div>
      <button class="contact-toggle" id="contact-toggle" aria-expanded="false" aria-controls="profile-details">{t('Contact &amp; links','联系方式与链接')} <span aria-hidden="true">⌄</span></button>
      <div class="profile-details" id="profile-details"><div class="profile-divider"></div><dl class="profile-facts">
      <div><dt>{icon('mail')} {t('Email','邮箱')}</dt><dd><a href="mailto:hanfei@westlake.edu.cn">hanfei@westlake.edu.cn</a></dd></div>
      <div><dt>{icon('link')} {t('Website','个人主页')}</dt><dd><a href="https://hanfei-hz.github.io/">hanfei-hz.github.io</a></dd></div>
      <div><dt>{icon('scholar')} {t('Research','研究方向')}</dt><dd>{t('Bioinspired propulsion &amp; robot learning','仿生推进与机器人学习')}</dd></div>
      <div><dt>{icon('cv')} {t('Expected graduation','预计毕业')}</dt><dd>{t('June 2027','2027 年 6 月')}</dd></div>
      <div><dt>{icon('link')} {t('Visiting research','访问研究')}</dt><dd>{t('Penn State University','宾夕法尼亚州立大学')}<span>{t('April – October 2026','2026 年 4 月—10 月')}</span></dd></div></dl>
      <ul class="links"><li>{external('https://scholar.google.com/citations?user=3WVj0IoAAAAJ',icon('scholar')+'Google Scholar').replace('<a ','<a class="pill" ')}</li><li>{external('https://github.com/HanFei-hz',icon('github')+'GitHub').replace('<a ','<a class="pill" ')}</li><li>{external('https://www.researchgate.net/profile/Fei-Han-60',icon('rg')+'ResearchGate').replace('<a ','<a class="pill" ')}</li><li><a class="pill pill-solid" href="#experience">{icon('cv')}{t('CVs in English &amp; Chinese','中英文简历')}</a></li></ul>
      <p class="profile-note">{t('Experiments, models and learning<br>for robots in real fluids.','以实验、建模与学习方法<br>研究真实流体中的机器人运动。')}</p></div></aside>'''
    about=f'''<p class="eyebrow">{t('Robotics · Learning · Fluid dynamics','机器人 · 学习 · 流体力学')}</p><h2 class="section-title">{t('About me','关于我')}</h2>
      <div class="intro-banner"><p class="intro-label">{t('Bioinspired propulsion and robot learning','仿生推进与机器人学习')}</p><h3>{t('Learning to move<br><em>in real fluids.</em>','在真实流体中<br><em>学习机器人运动。</em>')}</h3><p>{t('Experimental platforms, hydrodynamic models and learning-based control.','实验平台、水动力建模与学习控制。')}</p><a class="pill pill-solid" href="#research">{t('Explore my research','了解研究项目')} <span aria-hidden="true">↗</span></a><div class="flow-art" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div></div>
      <div class="bio"><p>{t('I am a PhD student in Computer Science and Technology at '+external('https://i4fsi.lab.westlake.edu.cn/','Westlake University’s i4FSI Lab')+', advised by Prof. Dixia Fan. I study bioinspired propulsion and robot learning, with expected graduation in June 2027.', '我是西湖大学计算机科学与技术专业博士研究生，师从范迪夏教授，在 '+external('https://i4fsi.lab.westlake.edu.cn/','i4FSI 实验室')+'开展仿生推进与机器人学习研究，预计于 2027 年 6 月毕业。')}</p>
      <p>{t('Since December 2023, I have pursued parallel research on the REEF propulsor platform and quadruped swimming, connecting force measurements, dynamics modeling, policy learning and robot experiments. My earlier work covers deep-sea soft grippers and storm-petrel locomotion.', '自 2023 年 12 月起，我并行开展 REEF 仿生推进器平台与四足机器人游动研究，贯通受力测量、动力学建模、策略学习和真机验证。此前研究包括深海软体机械手与海燕仿生运动。')}</p>
      <p>{t('My April–October 2026 visiting research at '+external('https://sites.psu.edu/libr/team/','Penn State University')+' focuses on reduced-order dynamics, numerical simulation and experiment design for multilegged swimming.', '2026 年 4 月至 10 月，我在'+external('https://sites.psu.edu/libr/team/','宾夕法尼亚州立大学')+'开展多足仿生游动的降阶动力学建模、数值仿真与实验设计。')}</p></div>
      <ul class="tags">{''.join('<li>'+x+'</li>' for x in t(['Robot learning','Hydrodynamic modeling','Bioinspired robotics','Soft robotics','Experimental systems'],['机器人学习','水动力建模','仿生机器人','软体机器人','实验系统']))}</ul>
      <section class="stats" aria-label="{t('Research at a glance','研究概览')}"><div><strong>8</strong><span>{t('papers published<br>or accepted','已发表或录用<br>论文')}</span></div><div><strong>3</strong><span>{t('manuscripts<br>under review','在审<br>稿件')}</span></div><div><strong>2016</strong><span>{t('started building<br>competition robots','开始参与<br>机器人竞赛')}</span></div><div><strong>2027</strong><span>{t('expected PhD<br>graduation','预计<br>博士毕业')}</span></div></section>
      <div class="section-heading"><h3>{t('Research in focus','研究重点')}</h3><a href="#research">{t('All projects','全部项目')} ↗</a></div><div class="focus-grid"><a class="focus-card" href="#research"><img src="./assets/img/shoal.jpg" alt="{t('SHOAL experimental platform','SHOAL 实验平台')}" width="1200" height="721"><div><span class="theme-kicker">{t('01 / Physical learning','01 / 真实流体学习')}</span><h4>{t('Experiments that inform learning','以真实实验支撑学习')}</h4><p>REEF · SHOAL · HydroWrench</p></div><span class="card-arrow" aria-hidden="true">↗</span></a><a class="focus-card" href="#videos"><img src="./assets/img/lts_outdoor.jpg" alt="{t('Quadrupedal swimming robot','四足游动机器人')}" width="1400" height="800"><div><span class="theme-kicker">{t('02 / Aquatic robotics','02 / 水下机器人')}</span><h4>{t('Models, policies and swimming robots','模型、策略与游动机器人')}</h4><p>{t('ICRA 2025 and 2026 demonstrations','ICRA 2025 与 2026 实验视频')}</p></div><span class="card-arrow" aria-hidden="true">↗</span></a></div>
      <section class="news-block" id="news"><div class="section-heading"><h3>{t('Recent updates','近期动态')}</h3><span class="muted">2026</span></div><ol class="news">
      <li><time>{t('Oct 2026','2026.10')}</time><p>{t('<strong>REEF</strong> is under review at <strong>Nature Mechanical Engineering</strong>. The manuscript is available on '+external('https://arxiv.org/abs/2609.14254','arXiv')+'.','<strong>REEF</strong> 在 <strong>Nature Mechanical Engineering</strong> 在审，稿件已公开于 '+external('https://arxiv.org/abs/2609.14254','arXiv')+'。')}</p></li>
      <li><time>{t('Sep 2026','2026.09')}</time><p>{t('<strong>From Gaits to Routes</strong> is under review at ICRA 2027; <strong>HydroWrench</strong> is under review at ICLR 2027.','<strong>From Gaits to Routes</strong> 在 ICRA 2027 在审；<strong>HydroWrench</strong> 在 ICLR 2027 在审。')}</p></li>
      <li><time>2026</time><p>{t('<strong>Swimming Under Constraints</strong> accepted to ICRA 2026; co-first and co-corresponding author.','<strong>Swimming Under Constraints</strong> 获 ICRA 2026 录用，本人为共同第一作者及共同通讯作者。')}</p></li></ol><details class="older-news"><summary>{t('Earlier updates','更早动态')}</summary><ol class="news"><li><time>{t('Apr 2026','2026.04')}</time><p>{t('Started the April–October visiting appointment at Penn State University.','开始在宾夕法尼亚州立大学进行 4 月至 10 月的访问研究。')}</p></li><li><time>2025</time><p>{t('<strong>Learn to Swim</strong> published at ICRA 2025.','<strong>Learn to Swim</strong> 发表于 ICRA 2025。')}</p></li><li><time>2023</time><p>{t('Storm-petrel learning research published in <em>Bioinspiration &amp; Biomimetics</em>.','海燕学习控制研究发表于 <em>Bioinspiration &amp; Biomimetics</em>。')}</p></li></ol></details></section>'''

    research='<h2 class="section-title">'+t('Research projects','研究项目')+'</h2><p class="section-intro">'+t('My work links experimental systems with models and learning algorithms. The REEF platform and quadruped swimmer are parallel parts of a continuing doctoral research program.', '我的研究连接实验系统、物理模型与学习算法。REEF 平台和四足游动机器人是持续博士研究中并行开展的两条工作线。')+'</p>'
    research+=theme(t('REEF and learning in real fluids','REEF 与真实流体中的学习'),t('Dec 2023 – present · Doctoral research','2023.12—至今 · 博士研究'),t('Contribute to the REEF platform and learning-control pipeline: synchronized experiments, force-feedback data, hydrodynamic modeling, imitation learning, offline learning and online adaptation. Related work develops HydroWrench, a dataset and benchmark for dynamic-load reconstruction.', '参与 REEF 平台与学习控制流程建设，开展同步实验、力反馈数据采集、水动力建模、模仿学习、离线学习及在线适应。相关研究进一步构建 HydroWrench 动态载荷重建数据集与评估基准。'),'shoal.jpg',t('SHOAL experimental array','SHOAL 实验阵列'),'Nature Mechanical Engineering · '+t('Under review','在审')+' / HydroWrench · ICLR 2027 · '+t('Under review','在审'))
    research+=theme(t('Quadruped swimming and robot learning','四足游动与机器人学习'),t('Dec 2023 – present · Parallel work with REEF','2023.12—至今 · 与 REEF 并行研究'),t('Collect experimental force data and build an LSTM hydrodynamic model for multi-objective gait optimization. Study safe reinforcement learning, leg-phase coordination, swimming behavior planning and skill distillation, connecting single-leg experiments with whole-robot validation.', '承担实验受力数据采集与处理，建立 LSTM 水动力模型并结合多目标优化设计游动步态；研究安全强化学习、四腿相位协调、游动行为规划与技能蒸馏，将单腿实验与整机验证衔接起来。'),'lts_outdoor.jpg',t('Quadrupedal swimming robot in an outdoor pond','池塘中的四足游动机器人'),'Learn to Swim · ICRA 2025 / Swimming Under Constraints · ICRA 2026 / From Gaits to Routes · ICRA 2027')
    research+=f'<div class="service-card"><h3>{t("Applied collaboration with DEEP Robotics","云深处北极科考机器人合作")}</h3><p class="project-date">{t("Arctic expedition application · Aug 2025","北极科考应用 · 2025.08")}</p><p>{t("The collaboration adopted my force-testing, modeling and motion-parameter-optimization framework. I participated in discussions on specialized foot design as a project contributor.","作为项目参与者，提供被采用的受力测试、建模与运动参数优化架构，并参与特殊足掌设计讨论。")}</p></div>'
    research+=heading('Visiting and earlier research','访学及早期研究')
    research+=f'<div class="service-card"><p class="project-date">{t("Apr – Oct 2026 · Pennsylvania State University","2026.04—2026.10 · 宾夕法尼亚州立大学")}</p><h3>{t("Multilegged swimming","多足生物游动与仿生研究")}</h3><p>{t("Visiting research on reduced-order dynamics, numerical simulation and experiment design for multilegged swimming.","访学期间开展多足仿生游动的降阶动力学建模、数值仿真与实验设计。")}</p></div>'
    research+=theme(t('Storm-petrel locomotion','海燕仿生运动研究'),t('Jul 2022 – Oct 2023 · Westlake University','2022.07—2023.10 · 西湖大学'),t('Combine air–water modeling with deep reinforcement learning to study pattering and sea-anchoring. This project began during my research-assistant appointment and continued into the beginning of my PhD.', '结合空水耦合建模与深度强化学习研究海燕踏水和海锚行为。该项目始于科研助理阶段，并延续至博士入学初期。'),'petrel_model.jpg',t('Storm-petrel morphological model','海燕形态与运动模型'),'Bioinspiration &amp; Biomimetics · 2023 · '+t('Co-first author','共同第一作者'),True)
    research+=theme(t('Deep-sea soft robotic gripper','深海软体机械手'),t('Sep 2019 – Jun 2022 · MEng research','2019.09—2022.06 · 硕士研究'),t('As a core student contributor, led structural design, fabrication, sensing and control development. Discussed technical approaches with my advisor and guided junior students in implementation and experiments. Also contributed to background research and preparation of project proposal materials.', '作为软体手方向主要学生参与者，主导结构设计、样机制作、感知与控制开发；与导师讨论技术方案，带领师弟妹开展实现与实验，并参与项目申请的前期调研和材料准备。'),'soft-gripper.jpg',t('Deep-sea soft gripper prototype','深海软体机械手样机'),t('NSFC Major Research Plan Integrated Project 92048302 · Fundamental Research on Robots Combining Rigid, Flexible and Soft Structures for Operations in Extreme Environments','国家自然科学基金重大研究计划集成项目 92048302 · 适应极端环境作业的刚-柔-软共融机器人基础研究'),True)
    research+=theme(t('RoboMaster development and team leadership','RoboMaster 开发与团队组织'),t('Sep 2016 – 2019 · Zhengzhou University','2016.09—2019 · 郑州大学'),t('Participated in the 2017, 2018 and 2019 seasons; captain in the 2017–2018 academic year and advisor in 2019. Developed STM32 hardware and C control software for infantry, hero, engineer, aerial and sentry robots. As captain, coordinated technical planning, task allocation, schedules and system integration.', '参加 2017、2018、2019 三届比赛，2017—2018 学年担任队长，2019 赛季以顾问身份参与。参与步兵、英雄、工程、无人机及哨兵机器人设计制造，负责 STM32 硬件及 C 语言底盘、云台与发弹控制开发；任队长期间统筹技术规划、分工、进度与系统联调。'),'robomaster-team.webp',t('RoboMaster robots and Zhengzhou University team','RoboMaster 机器人与郑州大学战队合照'),t('Embedded systems · Robot integration · Team coordination','嵌入式开发 · 机器人联调 · 团队协作'),True)

    publications=f'<div class="section-head"><h2 class="section-title">{t("Publications","论文成果")}</h2><div class="filters" role="group" aria-label="{t("Filter publications","筛选论文")}"><button class="chip is-active" data-filter="all">{t("All","全部")}</button><button class="chip" data-filter="published">{t("Published / accepted","已发表／录用")}</button><button class="chip" data-filter="review">{t("Under review","在审")}</button></div></div><p class="legend">{t("* Equal contribution · ✉ Corresponding author · My name is in bold.","* 表示共同第一作者 · ✉ 表示通讯作者 · 本人姓名加粗。")}</p>'
    for review in (False,True):
        publications+=f'<h3 class="pub-group" data-group="{"review" if review else "published"}">{t("Under review","在审稿件") if review else t("Published and accepted","已发表与已录用")}</h3><ol class="pubs">'
        for paper in PAPERS:
            if (paper['status']=='review')!=review: continue
            status={'published':t('Published','已发表'),'accepted':t('Accepted','已录用'),'review':t('Under review','在审')}[paper['status']]
            image=f'<figure class="pub-thumb"><img src="./assets/img/{paper["img"]}" alt="{escape(local(paper["title"]))}" loading="lazy"></figure>' if paper.get('img') else ''
            links=''
            for url,label in paper['links']:
                label={'Video':t('Video','视频'),'Code':t('Code','代码')}.get(label,label)
                links+=(f'<a href="{url}">{label}</a>' if url.startswith('#') else external(url,label))
            if paper.get('bib'): links+=f'<button data-bib="{paper["bib"]}">{icon("quote")}BibTeX</button>'
            authors=f'<p class="authors">{local(paper["authors"])}</p>' if paper.get('authors') else ''
            publications+=f'<li class="pub {"pub-compact" if not image else ""}" data-status="{"review" if review else "published"}">{image}<div class="pub-body"><p class="venue"><span class="badge badge-{"review" if review else "pub"}">{status}</span> {local(paper["venue"])}</p><h4>{local(paper["title"])}</h4>{authors}<p class="tldr">{local(paper["summary"])}</p><div class="pub-links">{links}</div></div></li>'
        publications+='</ol>'
    publications+=f'<p class="more">{t("Also on ","更多信息见 ")}{external("https://scholar.google.com/citations?user=3WVj0IoAAAAJ","Google Scholar")}.</p>'

    videos=f'<h2 class="section-title">{t("ICRA videos","ICRA 实验视频")}</h2><p class="section-intro">{t("Quadrupedal swimming experiments on hydrodynamic modeling, gait optimization and safe reinforcement learning.","展示四足机器人水动力建模、步态优化与安全强化学习的实验工作。")}</p><div class="videos">'
    for year,title in [(2025,'Learn to Swim'),(2026,'Swimming Under Constraints')]:
        videos+=f'<figure class="video-card" id="video-icra{year}"><div class="video-frame"><video controls preload="metadata" playsinline poster="./assets/img/icra{year}-video-poster.jpg"><source src="./assets/videos/icra{year}.mp4" type="video/mp4">{t("Your browser does not support HTML video.","你的浏览器不支持此视频格式。")}</video></div><figcaption><span class="badge badge-pub">ICRA {year}</span> {title}</figcaption></figure>'
    videos+='</div>'

    experience=f'<h2 class="section-title">{t("Education and experience","教育与经历")}</h2>'+heading('Education','教育经历')
    experience+=timeline([
      (t('Aug 2023 – Jun 2027 (expected)','2023.08—2027.06（预计）'),t('PhD · Westlake University','博士 · 西湖大学'),t('Computer Science and Technology · Advisor: Prof. Dixia Fan.','计算机科学与技术 · 导师：范迪夏教授。')),
      (t('Sep 2019 – Jun 2022','2019.09—2022.06'),t('MEng · University of Chinese Academy of Sciences','硕士 · 中国科学院大学'),t('Pattern Recognition and Intelligent Systems. Research at the State Key Laboratory of Robotics, Shenyang Institute of Automation, Chinese Academy of Sciences.','模式识别与智能系统。培养单位：中国科学院沈阳自动化研究所机器人学国家重点实验室。')),
      (t('Sep 2015 – Jul 2019','2015.09—2019.07'),t('BEng · Zhengzhou University','学士 · 郑州大学'),t('Measurement and Control Technology and Instruments.','测控技术与仪器。')),
    ])
    experience+=heading('Research appointments','科研任职')+timeline([
      (t('Apr – Oct 2026','2026.04—2026.10'),t('Visiting Scholar · Pennsylvania State University','访问学者 · 宾夕法尼亚州立大学'),t('Multilegged swimming: reduced-order models, numerical simulation and experiment design.','多足仿生游动：降阶建模、数值仿真与实验设计。')),
      (t('Jul 2022 – Aug 2023','2022.07—2023.08'),t('Research Assistant · Westlake University','科研助理 · 西湖大学'),t('Storm-petrel locomotion research, modeling, data analysis and scientific writing.','海燕仿生运动研究、建模、数据分析与论文撰写。')),
    ])
    experience+=heading('Research timeline','研究时间线')+timeline([
      (t('Dec 2023 – present','2023.12—至今'),t('Bioinspired propulsion and robot learning','仿生推进器与机器人学习'),t('REEF and quadruped swimming experiments developed in parallel; papers are milestones within this continuing research.','REEF 与机械狗游动实验并行推进，论文是持续研究中的阶段成果。')),
      (t('Jul 2022 – Oct 2023','2022.07—2023.10'),t('Storm-petrel locomotion','海燕仿生运动'),t('Research-assistant stage through early PhD study.','从科研助理阶段延续至博士入学初期。')),
      (t('Sep 2019 – Jun 2022','2019.09—2022.06'),t('Deep-sea soft robotic gripper','深海软体机械手'),t('Personal MEng research period; design, fabrication, sensing, control and proposal preparation.','个人硕士研究阶段，承担设计制作、感知控制及项目申请准备。')),
      (t('Sep 2016 – 2019','2016.09—2019'),t('RoboMaster','RoboMaster'),t('Captain, 2017–2018 academic year; advisor, 2019 season.','2017—2018 学年任队长，2019 赛季任顾问。')),
    ])
    experience+=heading('Download a CV','下载简历')+f'<p class="section-intro">{t("Two-page CVs with a homepage QR code. Choose the research context and language.","每份均为两页，带个人主页二维码。可按阅读场景和语言选择。")}</p><div class="cv-downloads">'
    for kind,title,body in [('industry',t('Industry research','企业科研版'),t('Projects, technical contributions and team leadership.','项目经历、技术贡献与团队组织。')),('academic',t('Academic research','高校科研版'),t('Research, publications and academic service.','研究工作、论文与学术服务。'))]:
        experience+=f'<article class="cv-option"><h3>{title}</h3><p>{body}</p><div class="pub-links"><a href="./assets/files/cv-{kind}-en.pdf" target="_blank" rel="noopener" lang="en">English PDF {icon("pdf")}</a><a href="./assets/files/cv-{kind}-zh.pdf" target="_blank" rel="noopener" lang="zh-CN">中文 PDF {icon("pdf")}</a></div></article>'
    experience+='</div>'+heading('Selected honors','部分竞赛荣誉')+'<ul class="achievement-list">'
    honors=[('2017 / 2018',t('RoboMaster · Third Prize in the 2017 Western Regional and 2018 Central Regional competitions.','RoboMaster：2017 西部赛区三等奖、2018 中部分区赛三等奖。')),('2017',t('National Undergraduate Electronics Design Contest · Second Prize, Henan Region, undergraduate division.','全国大学生电子设计竞赛：本科组河南赛区二等奖。')),('2018',t('Zhengzhou University “Creating Youth” Entrepreneurship Competition · Special Prize for the 3D Scanner project.','郑州大学第三届“创青春”创业大赛：《三维扫描仪》项目特等奖。'))]
    experience+=''.join(f'<li><time>{date}</time><p>{body}</p></li>' for date,body in honors)+'</ul>'

    services=[
      (t('IROS 2025 campus visits and exchange','IROS 2025 期间校访与学术交流'),t('As a core organizer and presenter for laboratory-hosted visits to Westlake University, welcomed professors, researchers and industry guests. Introduced the university, laboratory research and results, and discussed bioinspired robotics, fluid mechanics and intelligent control.','作为实验室组织西湖大学参观及学术交流活动的主要组织和讲解人员，接待国内外高校与企业来访人员，介绍学校、实验室研究方向与成果，并围绕仿生机器人、流体力学和智能控制交流。')),
      (t('Laboratory open days and science outreach','实验室开放与中小学科普'),t('Repeatedly hosted primary and secondary school visits organized by the School of Engineering, introducing research platforms and explaining bioinspired robotics and fluid mechanics.','多次参与工学院面向中小学生的实验室开放与科普活动，承担参观接待、科研平台介绍，以及仿生机器人和流体力学现场讲解。')),
      (t('Conference volunteering','智能流体学术会议志愿服务'),t('Supported conference organization and on-site service at an intelligent-fluids academic meeting hosted by the School of Engineering.','担任工学院承办的智能流体学术会议志愿者，参与会务组织与现场服务。')),
      (t('Undergraduate residential-college exchanges','本科生书院交流'),t('Shared research experiences and reflections on postgraduate study as a senior graduate student, helping undergraduates explore research and future study.','以研究生学长身份参与书院交流，分享科研经历、研究过程中的思考和研究生发展路径，帮助本科生了解科研学习。')),
      (t('Westlake University Xinyue Choir','西湖大学心乐合唱团'),t('Participated in group rehearsals and university performances, learning through musical practice and collaboration.','参与合唱团集体排练及学校演出，在音乐实践中培养艺术素养与团队协作能力。')),
      (t('Exercise and life outside research','体育锻炼与课余生活'),t('Maintain regular exercise alongside research, with interests in badminton, fitness, singing and photography.','在科研之外保持规律体育锻炼，喜欢羽毛球、健身、唱歌和摄影。')),
    ]
    life=f'<h2 class="section-title">{t("Service and community","公共服务与校园参与")}</h2><p class="section-intro">{t("Teaching through outreach, organizing exchanges and contributing to campus life are part of my development as a researcher.","在科研之外，通过科普讲解、交流组织、公共服务和文体活动参与校园生活。")}</p><div class="service-grid">'+''.join(f'<article class="service-card"><h3>{title}</h3><p>{body}</p></article>' for title,body in services)+'</div>'
    life+=heading('Engineering memories','工程实践影像')+f'<div class="archive-gallery"><figure><img src="./assets/img/robomaster-team.webp" alt="{t("RoboMaster team and robot platforms","RoboMaster 团队与机器人平台")}" loading="lazy"><figcaption>{t("RoboMaster robots and team during undergraduate study.","本科阶段参与的 RoboMaster 机器人与团队。")}</figcaption></figure><figure><img src="./assets/img/soft-gripper-control.webp" alt="{t("Data-glove interaction with a soft robotic hand","数据手套与软体机械手的人机交互实验")}" loading="lazy"><figcaption>{t("Data-glove interaction experiments with the soft gripper during MEng research.","硕士阶段的数据手套与软体机械手交互实验。")}</figcaption></figure></div>'
    life+=heading('Code and tools','代码与工具')+'<ul class="repos">'
    for url,title,desc in [('https://github.com/HanFei-hz/Dog_LSTM','Dog_LSTM',t('LSTM hydrodynamics and gait optimization','LSTM 水动力建模与步态优化')),('https://github.com/HanFei-hz/Leg_offlineDRL','Leg_offlineDRL',t('Offline reinforcement learning for a swimming leg','单腿游动离线强化学习')),('https://github.com/HanFei-hz/WaterLily','WaterLily',t('CFD experiments for flapping and undulating bodies','拍动与波动体 CFD 实验')),('./assets/files/rl_explorer.html','RL Explorer',t('Interactive reinforcement-learning knowledge graph (English)','强化学习交互知识图谱（英文）'))]:
        life+=f'<li>{external(url,"<b>"+title+"</b><span>"+desc+"</span>")}</li>'
    life+='</ul>'
    panels=''.join(f'<section class="panel" id="{id}" aria-labelledby="tab-{id}" tabindex="0">{body}</section>' for id,body in [('about',about),('research',research),('publications',publications),('videos',videos),('experience',experience),('life',life)])
    return f'''<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t('Fei Han · Robot Learning and Bioinspired Robotics','韩非 · 机器人学习与仿生机器人')}</title><meta name="description" content="{escape(description,quote=True)}"><meta property="og:title" content="{t('Fei Han · Robotics Research','韩非 · 机器人研究')}"><meta property="og:description" content="{escape(description,quote=True)}"><meta property="og:image" content="https://hanfei-hz.github.io/assets/img/shoal.jpg"><meta property="og:url" content="{page_url}"><meta property="og:locale" content="{t('en_US','zh_CN')}">
<link rel="canonical" href="{page_url}"><link rel="alternate" hreflang="en" href="https://hanfei-hz.github.io/"><link rel="alternate" hreflang="zh-CN" href="https://hanfei-hz.github.io/zh.html"><link rel="alternate" hreflang="x-default" href="https://hanfei-hz.github.io/"><link rel="icon" href="./assets/favicon.svg" type="image/svg+xml">
<script>document.documentElement.dataset.theme='dark';try{{var t=localStorage.getItem('theme');if(t==='light'||t==='dark')document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
<script src="./assets/js/language.js?v={VERSION}"></script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&display=swap" rel="stylesheet"><link rel="stylesheet" href="./assets/css/main.css?v={VERSION}"></head>
<body><a class="skip-link" href="#about">{t('Skip to content','跳至正文')}</a>{ICONS}
<div class="site-shell" id="top">{profile}<main class="content-card" id="main-content"><header class="panel-toolbar"><nav class="tab-nav" aria-label="{t('Main sections','主要栏目')}">{nav}</nav><button class="icon-btn" id="theme-toggle" aria-label="{t('Switch color theme','切换明暗主题')}"><svg class="ic ic-moon" aria-hidden="true"><use href="#i-moon"/></svg><svg class="ic ic-sun" aria-hidden="true"><use href="#i-sun"/></svg></button></header>{panels}
<footer class="footer"><p>© 2026 {t('Fei Han','韩非')}</p><p>{t('Updated October 2026','更新于 2026 年 10 月')}</p></footer></main></div>
<dialog class="bib-dialog" id="bib-dialog"><form method="dialog"><div class="bib-head"><strong>BibTeX</strong><div><button type="button" class="chip" id="bib-copy">{t('Copy','复制')}</button><button class="chip">{t('Close','关闭')}</button></div></div><pre id="bib-text"></pre></form></dialog>
{BIB}
<script src="./assets/js/main.js?v={VERSION}"></script>
<!-- Cloudflare Web Analytics -->
<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "4a9b78b9961f4cfc9258f3010cb69058"}}'></script>
<!-- End Cloudflare Web Analytics -->
</body></html>'''

if __name__=='__main__':
    for filename,zh in [('index.html',False),('zh.html',True)]:
        destination=(ROOT/filename).resolve()
        assert destination.is_relative_to(ROOT)
        destination.write_text(build(zh),encoding='utf-8')
        print(filename)
