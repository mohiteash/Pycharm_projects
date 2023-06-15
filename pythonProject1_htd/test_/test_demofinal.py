from POM.demo_electronics import DemoFile

class TestDemo:
    def test_demoelec(self,_driver):
        demo = DemoFile(_driver)
        demo.demo_camera()
        demo.cam_dispaly()
        demo.cam_view()
        demo.cam_filter()
        demo.cam_des()
        demo.cell_sort()
        demo.cell_display()
        demo.cell_view()
        demo.cell_des()
        demo.cell_addto()











