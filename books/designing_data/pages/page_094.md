## page_094

the encoding. This takes time, can be error-prone, and becomes frustrating when there are many values that need to be decoded.

The alternative suddenly becomes quite attractive: just directly label all entities with their values and properties, and you're done. Information at the point of need! No change of focus and no dereferencing required! This must be the superior solution, right?

Well, yes and no. Labels on the data points absolutely make the labeled knowledge more accessible, but only if you can easily read the labels and tell which entities they're attached to. Labels can be obfuscated by if there are a large number of data points located very close together. If the visual density that already exists is compounded by a flock of labels, you haven't improved your clarity at all.

So what's the bottom line? Context. It all depends on how many total data points you're dealing with, and how many possible values exist for those data points. Fewer data points or less dense layouts are more likely candidates for direct labeling, because you've got room to add the label text. This is true regardless of the number of values, though more different values benefit from direct labeling, because a key becomes cumbersome when it's got too many values to address. Conversely, a range of fewer possible values, regardless of the number of points, can be well served by a key, because there are fewer values the key has to address.

The trickiest situation is one with many, densely-located data points and many values. In this last situation, direct labels can add visual noise, and a key can become large, unwieldy, and hard to use. Consider, then, labeling only some values, or allowing your reader to turn some or all labels on and off as necessary.

![image](/images/page_094_img_001.png)

One set of labels that should always be present is the labels on your axes. These help the reader in a variety of ways; see “Position: Layout and Axes” on page 47.

Pitfalls to Avoid

Communication is the primary goal of data visualization. Any element that hinders—rather than helps—the reader, then, needs to be changed or removed: labels and tags that are in the way, colors that confuse or simply add no value, uncomfortable scales or angles. Each element needs to serve a particular purpose toward the goal of communicating and explaining information. Efficiency matters, because if you're wasting a viewer's time or energy, they're going to move on without receiving your message.

Here are some elements and effects that need to be used judiciously in some cases and avoided at all costs in others. In general, a good rule of thumb for these is: if you're not using these elements for a very specific reason (and/or your reason is “they look cool”), then do yourself and your reader a favor and steer clear of them.

Chapter 6: Apply Your Encodings Well

80

---

