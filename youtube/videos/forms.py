from django import forms

class VideoUploadForm(forms.Form):

    title = forms.CharField(max_length= 100,
                            widget= forms.TextInput(
                                    attrs= {
                                        "class" : "forms.input",
                                        "placeholder" : "Enter Your Video Tittle"} )
    )

    description = forms.CharField(required= False, max_length= 500,
                                  widget = forms.TextArea(
                                      attrs={
                                          "class" : "forms.input",
                                          "palceholder" : "Enter Your Video Description",
                                          "rows" : 4} )
    )

    video_file = forms.FileField(
        widget= forms.FileInput(
            attrs={
                "class" : "form-input",
                "accept" : "videos/*"
            })
    )

    def clean_video_file(self):
        video = self.cleaned_data.get("video_file")

        if video:
            if video.size > 100 * 1024 * 1024:
                raise forms.ValidationError("Size must be under 100 MB")
            
            allowed_types = ["video/mp4", "video/webm", "video/quicktime", "video/wmv"]
            if video.content_type not in allowed_types:
                raise forms.ValidationError("Unsupported Video type.")
        
        return video