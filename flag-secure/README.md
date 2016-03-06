Adding ```FLAG_SECURE``` on an Android activity wont let your users take screenhots or screenrecords of the current activity

# Usage
```java
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE,
      WindowManager.LayoutParams.FLAG_SECURE);
    setContentView(R.layout.activity_flagsecure);
  }
```

# Testing 

The test implemented is quite simple, we just use appium to open the activity and take some screenshot
with the FLAG_SECURE enabled and disabled. While the FLAG_SECURE is enable, the screenshot taken
by appium will be Zero bytes, otherwise taking screenshot would be available and the size of the 
file would be >0.

```python 
  self.driver.save_screenshot(PATH('./screen.png'))
  sleep(.5)
  size = os.stat(PATH('./screen.png')).st_size
  self.assertNotEqual(0, size)
        
  el = self.driver.find_element_by_id("secureBtt")
  el.click()
  sleep(.5)
  self.driver.save_screenshot(PATH('./screen_secure.png'))
  sleep(.5)
  size = os.stat(PATH('./screen_secure.png')).st_size
  self.assertEqual(0, size)
```
