import qrcode
# imports pillow by default 

class MyQR: 
    def __init__(self, size:int, padding: int): 
        self.qr = qrcode.QRCode(box_size=size, border=padding)
        
    def create_qr(self, file_name, fg, bg):
        user_input = input('Enter some text: ')
        try: 
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
            
            print(f'Sucessfully created! {file_name}')
        except Exception as e: 
            print(f'Error: {e}')

def main(): 
    myqr = MyQR(30, 2)
    myqr.create('sample.png', fg='black', bg='white')
    
if __name__ == '__main__':
    main()