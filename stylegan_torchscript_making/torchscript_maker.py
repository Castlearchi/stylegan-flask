import torch
from models.stylegan_generator import StyleGANGenerator

resolution = 1024
model = StyleGANGenerator(resolution)

# weights and bias sets
checkpoint_path = "models/stylegan_ffhq1024.pth"
checkpoint = torch.load(checkpoint_path, map_location="cpu")
model.load_state_dict(checkpoint["generator_smooth"])

model.eval()

# sampleinput
test_sample_input_trace = torch.randn(1, 512)

scripted_model = torch.jit.trace(model, test_sample_input_trace)
print("torch.jit.trace  ", isinstance(scripted_model, torch.jit.ScriptModule))
scripted_model.save("../app/src/stylegan_ffhq1024.pt")
