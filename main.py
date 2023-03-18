import pikepdf
import streamlit as st
from pypdf import PdfWriter

st.title("Secured Simple PDF merger")

def main():

    option = st.selectbox('Merge PDF Here', ('Merge PDF','Merge PDF'))

    if option == 'Merge PDF':
        uploaded_files = st.file_uploader("Files will be merged in the order of selection", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename: ",uploaded_file.name)

        merge=st.button("Merge")

        if merge:
            merger = PdfWriter()
            for pdf in uploaded_files:
                merger.append(pdf)
                merger.write("Merged_PDF.pdf")

            with open("Merged_PDF.pdf", "rb") as f:
                PDFbyte = f.read()

            st.download_button(label="Download PDF",
                               data=PDFbyte,
                               file_name="Merged_PDF.pdf",
                               mime='application/octet-stream')


if __name__ == '__main__':
    main()
