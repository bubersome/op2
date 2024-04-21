```
执行命令: ['whisper', '.\\投資心理學｜THE PSYCHOLOGY OF INVESTING.m4a', '--device', 'cuda', '--model', 'large-v1', '--language', 'en']    
程序终止。
Traceback (most recent call last):
  File "C:\Users\70win\.conda\envs\whisper\lib\runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Users\70win\.conda\envs\whisper\lib\runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "C:\Users\70win\.conda\envs\whisper\Scripts\whisper.exe\__main__.py", line 7, in <module>
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\whisper\transcribe.py", line 478, in cli
(whisper) PS C:\Users\70win\Videos\m4a>     result = transcribe(model, audio_path, temperature=temperature, **args)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\whisper\transcribe.py", line 240, in transcribe
    result: DecodingResult = decode_with_fallback(mel_segment)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\whisper\transcribe.py", line 170, in decode_with_fallback
    decode_result = model.decode(segment, options)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\torch\utils\_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\whisper\decoding.py", line 824, in decode
    result = DecodingTask(model, options).run(mel)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\torch\utils\_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\whisper\decoding.py", line 737, in run
    tokens, sum_logprobs, no_speech_probs = self._main_loop(audio_features, tokens)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\whisper\decoding.py", line 687, in _main_loop
    logits = self.inference.logits(tokens, audio_features)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\whisper\decoding.py", line 163, in logits
    return self.model.decoder(tokens, audio_features, kv_cache=self.kv_cache)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\torch\nn\modules\module.py", line 1501, in _call_impl
    return forward_call(*args, **kwargs)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\whisper\model.py", line 211, in forward
    x = block(x, xa, mask=self.mask, kv_cache=kv_cache)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\torch\nn\modules\module.py", line 1501, in _call_impl
    return forward_call(*args, **kwargs)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\whisper\model.py", line 136, in forward
    x = x + self.attn(self.attn_ln(x), mask=mask, kv_cache=kv_cache)[0]
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\torch\nn\modules\module.py", line 1501, in _call_impl
    return forward_call(*args, **kwargs)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\whisper\model.py", line 84, in forward
    v = self.value(x if xa is None else xa)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\torch\nn\modules\module.py", line 1538, in _call_impl
    result = forward_call(*args, **kwargs)
  File "C:\Users\70win\.conda\envs\whisper\lib\site-packages\whisper\model.py", line 37, in forward
    return F.linear(
KeyboardInterrupt
```

