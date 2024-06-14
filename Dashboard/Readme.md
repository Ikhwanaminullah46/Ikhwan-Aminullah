# Proyek Pertama: Menyelesaikan Institusi Pendidikan
---
## Business Understanding
---
Institut Jaya Jaya Maju merupakan suatu institusi pendidikan yang telah memiliki reputasi untuk mencetak banyak lulusan-lulusan bagus. Meskipun demikian, masih tedapat banyak siswa yang tidak dapat menyelesaikan studinya atau disebut _dropout_. 

### Permasalahan Bisnis
Institut Jaya Jaya Maju masih memiliki banyak siswa yang melakukan _dropout_. Jika dibiarkan, hal ini dapat berakibat buruk terutama dalam jangka panjang. Reputasi institut dalam kualitas pendidikannya, terutama dalam mengakomodir peningkatan kualitas siswanya jadi dipertanyakan. Situasi tersebut dapat membuat institusi kehilangan banyak potensi dan peluang misalnya untuk mengadakan kerja sama dengan industri, maupun menarik minat siswa kedepannya.

### Cakupan Proyek
Cakupan dari proyek ini meliputi Data Preparation, EDA, Analisis Dropout, Modelling, Evaluation, Deployment pada streamlit, serta pembuatan dashboard pada tableau public.

Batasan proyek: Proyek ini hanya menggunakan dataset yang disediakan tanpa menggabungkan dengan  sumber eksternal.

Keluaran dari proyek ini adalah rekomendasi aksi yang dapat dilakukan untuk mengatasi jumlah siswa yang dropout, model machine learning yang di deploy menggunakan streamlit cloud, dan juga sebuat business dashboard untuk menampilkan faktor-faktor terkait dengan lulus tidaknya siswa untuk keperluan monitoring dan analisis lebih lanjut.

### Persiapan
Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Setup environment:
pipenv install
pipenv shell
pip install requirements.txt
jupyter notebook

## Business Dashboard
---
Pada dashboard yang dibuat, terdapat beberapa faktor yang dapat mendeskripsikan karakteristik siswa-siswa yang dropout maupun graduate. Dashboard juga dilengkapi dengan fitur filter, dimana dashboard dapat difilter dengan menekan filter terkait

link dashboard: https://public.tableau.com/views/StudentPerformance_17182164843200/StudentPerformanceDashboard?:language=enUS&:sid=&:display_count=n&:origin=viz_share_link

## **Conclusion**
1. Secara umum, siswa-siswa yang dropout memiliki rerata umur sekitar 24 tahun dan kebanyakan berjenis kelamin pria.
2. Siswa-siswa yang menghadiri kelas sore/malam (evening) memiliki tingkat dropout yang lebih tinggi. Ini kemungkinan disebabkan oleh siswa-siswa tersebut memiliki kegiatan lain seperti bekerja sehingga mempersulit mereka untuk fokus pada pembelajaran mereka. Kondisi ini juga didukung fakta bahwa siswa kelas malam memiliki rentang umur yang tinggi dibandingkan dengan kelas pagi-siang, yang menunjukkan bahwa mereka memiliki kegiatan lainnya pada waktu tersebut.
3. Siswa yang mengambil utang untuk bisa belajar pada institusi juga memiliki kemungkinan yang lebih tinggi untuk dropout. Ini dapat disebabkan oleh masalah finansial yang mengganggu fokus mereka untuk belajar.
4. Siswa yang dropout menghadiri lebih sedikit kelas dan juga nilai yang lebih buruk.

## **Recommended Actions**
1. Add Interview to the admission process. This will help to assess the future students motivations and commitment to finish their study. Giving students academic supervisors also help to monitor their academic progress.
2. Make more scholarship programs. Students with scholarship has a better academic performance and are very likely to graduate. These scholarships will also help students with financial problem, which will help them to focus more on their studies and eventually finish their studies and graduate.
3. Buddy Program is recommended to help address students academic performance problems such as lower grade and hopefully their motivation to complete their study. Students will be paired or put into a group that will help each other to study and motivate each other. This well boost students academic grades and boost their likelihood of completing studies.

1. Menambahkan wawancara ketika proses penerimaan siswa. Cara ini dapat membantu untuk menilai calon siswa terkait motivasi dan komitmen mereka untuk menyelesaikan pembelajaran mereka. Memberikan siswa-siswa pembimbing akademik juga dapat membantu mengawasi performa akademis mereka.
2. Mengadakan lebih banyak program beasiswa. Siswa yang mendapatkan beasiswa memiliki performa yang lebih baik dan mayoritas akan lulus tepat waktu. Program beasiswa ini juga dapat membantu siswa-siswa yang memiliki masalah finansial, sehingga mereka tidak perlu mengambil utang dan fokus pada pembelajaran.
3. Menerapkan program teman juga direkomendasikan untuk mengatasi performa akademik siswa yang buruk. Selain mengatasi akademik yang buruk, siswa-siswa yang telah dipasang-pasangkan ataupun dimasukkan kedalam kelompok dapat saling membantu terkait studi dan memotivasi satu sama lain. Program ini dapat membantu meningkatkan nilai akademis siswa dan kemungkinan mereka menyelesaikan studinya.
